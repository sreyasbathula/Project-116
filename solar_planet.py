import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",
            (70,50),
            cv2.FONT_HERSHEY_COMPLEX,
            0.9,
            (0,0,255)
            )

cv2.putText(img,
            "Mercury",
            (130,180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (255,255,255)
            )

cv2.putText(img,
            "Venus",
            (200,180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (255,255,255)
            )

cv2.putText(img,
            "Earth",
            (290,180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (255,255,255)
            )

cv2.putText(img,
            "Mars",
            (380,180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (255,255,255)
            )

cv2.putText(img,
            "Jupiter",
            (480,70),
            cv2.FONT_HERSHEY_COMPLEX,
            0.9,
            (255,255,255)
            )

cv2.putText(img,
            "Saturn",
            (750,100),
            cv2.FONT_HERSHEY_COMPLEX,
            0.8,
            (255,255,255)
            )

cv2.putText(img,
            "Uranus",
            (950,145),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Neptune",
            (1100,150),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.imshow("output",img)
cv2.waitKey(0)



cv2.imwrite("Solar_systemwithname.jpg",img)



