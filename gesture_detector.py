import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# Landmark indices for tips and PIP joints (knuckles)
FINGER_TIPS  = [8, 12, 16, 20]   # index, middle, ring, pinky tips
FINGER_PIPS  = [6, 10, 14, 18]   # their middle knuckles
THUMB_TIP    = 4
THUMB_IP     = 3


class GestureDetector:
    def __init__(self):
        self.hands = mp_hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

    def _fingers_up(self, lm):
        """
        Returns list of booleans [index, middle, ring, pinky]
        True = finger is extended/up
        """
        up = []
        for tip, pip in zip(FINGER_TIPS, FINGER_PIPS):
            # tip.y < pip.y means finger pointing UP (y increases downward)
            up.append(lm[tip].y < lm[pip].y)
        return up  # [index, middle, ring, pinky]

    def _thumb_up(self, lm):
        # Thumb: compare tip x vs IP joint x (works for right hand)
        return lm[THUMB_TIP].x < lm[THUMB_IP].x

    def detect_gesture(self, lm):
        """
        Returns: 'up' | 'down' | 'stop' | None
        """
        fingers = self._fingers_up(lm)
        index, middle, ring, pinky = fingers

        # ✋ Open palm — 4 fingers all up
        if index and middle and ring and pinky:
            return 'stop'

        # ☝️ Only index up, rest folded
        if index and not middle and not ring and not pinky:
            return 'up'

        # 👇 All fingers folded (fist) = scroll down
        if not index and not middle and not ring and not pinky:
            return 'down'

        return None  # ambiguous gesture, ignore

    def process(self, frame_rgb):
        """
        Returns: (gesture_str, hand_landmarks_or_None)
        gesture_str: 'up' | 'down' | 'stop' | None
        """
        results = self.hands.process(frame_rgb)

        if not results.multi_hand_landmarks:
            return None, None

        hand = results.multi_hand_landmarks[0]
        lm = hand.landmark

        gesture = self.detect_gesture(lm)
        return gesture, hand

    def draw(self, frame, hand_landmarks):
        mp_draw.draw_landmarks(
            frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
        )