import cv2
import mediapipe as mp
from pynput.keyboard import Key, Controller
import time

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)
mp_draw = mp.solutions.drawing_utils

# Initialize OpenCV video capture (lower resolution to reduce lag)
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 360)

# Initialize keyboard controller
keyboard = Controller()

# Finger tip indices for gesture detection
ungliya = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky
gesture_history = []
last_action = ""
prev_time = 0

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Camera nhi khul rha h!!!")
        continue

    # Flip the image for mirror view & convert to RGB
    image = cv2.flip(image, 1)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_rgb.flags.writeable = False
    results = hands.process(image_rgb)
    image_rgb.flags.writeable = True
    image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

    fingers_up = 0

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Thumb (check x position)
            if hand_landmarks.landmark[ungliya[0]].x > hand_landmarks.landmark[ungliya[0] - 2].x:
                fingers_up += 1

            # Other fingers (check y position)
            for tip_id in ungliya[1:]:
                if hand_landmarks.landmark[tip_id].y < hand_landmarks.landmark[tip_id - 2].y:
                    fingers_up += 1

    # Update gesture history for smoothing
    gesture_history.append(fingers_up)
    if len(gesture_history) > 5:
        gesture_history.pop(0)
    avg_fingers = sum(gesture_history) / len(gesture_history)

    # Control based on average gesture
    if avg_fingers >= 3:
        if last_action != "right":
            keyboard.press(Key.right)
            keyboard.release(Key.left)
            last_action = "right"
        cv2.putText(image, "Accelerate (Right)", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    elif avg_fingers < 3 and len(gesture_history) == 5:
        if last_action != "left":
            keyboard.press(Key.left)
            keyboard.release(Key.right)
            last_action = "left"
        cv2.putText(image, "Brake (Left)", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    else:
        keyboard.release(Key.left)
        keyboard.release(Key.right)
        cv2.putText(image, "No Hand Detected", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Calculate and display FPS
    current_time = time.time()
    fps = 1 / (current_time - prev_time) if (current_time - prev_time) > 0 else 0
    prev_time = current_time
    cv2.putText(image, f"FPS: {int(fps)}", (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

    # Show image
    cv2.imshow("Gesture-Controlled Hill Bike Racing", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
hands.close()