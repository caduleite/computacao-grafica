import cv2
import numpy as np

# Ler as duas imagens :
img1 = cv2.imread('solo.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('analysis.jpg', cv2.IMREAD_GRAYSCALE)

# Orb:
orb = cv2.ORB_create()
kp1, desc1 = orb.detectAndCompute(img1, None)
kp2, desc2 = orb.detectAndCompute(img2, None)

# Matches:
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(desc1, desc2)
matches = sorted(matches, key = lambda x:x.distance)


# Desenhar pontos correspondentes:
matching_result = cv2.drawMatches(img1, kp1, img2, kp2, matches[:50], None, flags=2)

#for m in matches:
 # print(m.distance)

  # print(len(matches))
  
#for d in desc1:
#print(d)

# Exibir imagens tratadas:
cv2.imwrite('img1.jpg', img1)
cv2.imwrite('img2.jpg', img2)
cv2.imwrite('mat_res.jpg', matching_result)