import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
import cProfile
import glob
import sys, os

# @profile
def pre_process_ans(srcpath, dstpath, filename):
    try:
        error = "ไม่พบกรอบ หรือ QRcode ของกระดาษคำตอบที่ไฟล์ : "+filename
        isExist = os.path.exists(dstpath)
        if isExist == False:
            os.mkdir(dstpath)
        
        # Load the img and convert to gray scale
        img = cv2.imread(srcpath+filename)
        img = img[10:img.shape[0]-10, 10:img.shape[1]-10]
        height, width, ch = img.shape
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray_img = cv2.GaussianBlur(gray_img, (5, 5), 0)
        # thresholding image
        thresh, th = cv2.threshold(gray_img, 150, 255, cv2.THRESH_BINARY_INV)
        kernel = np.ones((5, 5), np.uint8)
        for i in range(0, 2):
            for ii in range(1, 2):
                th = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel, iterations=i)
                th = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel, iterations=ii)
                # blurred = cv2.GaussianBlur(gray_img, (5, 5), 0)
                # edged = cv2.Canny(blurred, 30, 100)
                
                contours, hierarchy = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                largest = None
                max_area = 0
                for i in contours:
                    area = cv2.contourArea(i)
                    if area > max_area:
                        epsilon = 0.01 * cv2.arcLength(i, True)
                        approx = cv2.approxPolyDP(i, epsilon, True)
                        # cv2.drawContours(img, [approx], -1, (0, 255, 0), 2)
                        # plt.imshow(img, cmap='gray')
                        # plt.show()
                        if len(approx) == 4:
                            largest = approx
                            max_area = area
                            # cv2.drawContours(crop_img, [approx], -1, (0, 255, 0), 2)
                            # cv2.imshow("", crop_img)
                            # cv2.waitKey(1000)

                # cv2.imshow("", crop_img)
                # cv2.waitKey(0)
                # Reshape the largest contour to get the corner points
                if largest is None:
                    # return "Error : Corner not found at file: "+filename
                    return error
                else: 
                    break
            if largest is not None:
                break
        
        points = largest.reshape(4, 2)

        # Initialize an array to hold the reordered points
        input_points = np.zeros((4, 2), dtype="float32")

        # Calculate the sum of x and y coordinates
        points_sum = points.sum(axis=1)
        input_points[0] = points[np.argmin(points_sum)]
        input_points[3] = points[np.argmax(points_sum)]

        # Calculate the difference of x and y coordinates
        points_diff = np.diff(points, axis=1)
        input_points[1] = points[np.argmin(points_diff)]
        input_points[2] = points[np.argmax(points_diff)]

        if width < height:
            pts2 = np.array([[0, 0], [992, 0], [0, 1403], [992, 1403]], dtype=np.float32)
            output_size = (992, 1403)
        else:
            pts2 = np.array([[0, 0], [1403, 0], [0, 992], [1403, 992]], dtype=np.float32)
            output_size = (1403, 992)

        M = cv2.getPerspectiveTransform(input_points, pts2)
        dst = cv2.warpPerspective(img, M, output_size)
            
        # plt.subplot(234, xticks=[], yticks=[])
        # plt.title("PerspectiveTransform")
        # plt.imshow(dst, cmap="gray")

        # Third Section ===================================================================

        # Fourt Section ===================================================================

        gray_dst = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
        threshold, th = cv2.threshold(gray_dst, 150, 255, cv2.THRESH_BINARY)
        height_th, width_th, ch = dst.shape

        mask1 = np.zeros(th.shape[:2], np.uint8)
        mask1[0:35, 0:35] = 255

        mask2 = np.zeros(th.shape[:2], np.uint8)
        mask2[height_th-35:height_th, 0:35] = 255

        mask3 = np.zeros(th.shape[:2], np.uint8)
        mask3[0:35, width_th-35:width_th] = 255

        mask4 = np.zeros(th.shape[:2], np.uint8)
        mask4[height_th-35:height_th, width_th-35:width_th] = 255

        mask = [mask1, mask2, mask3, mask4]

        rt = None
        havecon = False
        rotation = 0
        for i in range(4):
            # masked_img = cv2.bitwise_and(th, th, mask=mask[i])
            # cv2.imshow("", masked_img)
            # cv2.waitKey(1000)
            # cv2.destroyAllWindows()
            hist_mask = cv2.calcHist([th], [0], mask[i], [2], [0, 256])
            if hist_mask[0] > 400 and hist_mask[0] < 1000:
                rt = i
                havecon = True

        if havecon == True:
            if rt == 0:
                rotation = 180
            elif rt == 1:
                rotation = 90
            elif rt == 2:
                rotation = -90
            elif rt == 3:
                rotation = 0
        else:
            # return "Error : QRcode not found or QRcode not in corner at file: "+filename
            return error
            

        scale = 1
        w = dst.shape[1]
        h = dst.shape[0]
        rangle = np.deg2rad(rotation)  # Convert rotation angle to radians

        # Calculate new image width and height after rotation
        nw = (abs(np.sin(rangle)*h) + abs(np.cos(rangle)*w))*scale
        nh = (abs(np.cos(rangle)*h) + abs(np.sin(rangle)*w))*scale

        # Calculate rotation matrix and translation
        rot_mat = cv2.getRotationMatrix2D((nw*0.5, nh*0.5), rotation, scale)
        rot_move = np.dot(rot_mat, np.array([(nw-w)*0.5, (nh-h)*0.5, 0]))

        # Update translation part of the transform matrix
        rot_mat[0, 2] += rot_move[0]
        rot_mat[1, 2] += rot_move[1]

        # Apply the rotation transformation to the image
        dst = cv2.warpAffine(dst, rot_mat, (int(math.ceil(nw)), int(math.ceil(nh))), flags=cv2.INTER_LANCZOS4)
            
        # Fourt Section ===================================================================
        
        cv2.imwrite(dstpath+"pre_"+filename.split(".")[0]+".jpg", dst)
        # plt.subplot(235, xticks=[], yticks=[])
        # plt.title("Rotate_2")
        # plt.imshow(dst, cmap="gray")
        # plt.subplot(236, xticks=[], yticks=[])
        # plt.title("Result")
        # plt.imshow(dst, cmap="gray")
        # plt.show()

        return True
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        return "Error Line "+str(exc_tb.tb_lineno if exc_tb else None)+" : "+str(e)+" at file: "+filename
    
# if __name__ == '__main__':
#     img_list = []
#     c = 0
#     for filename in glob.glob('image/From_T_Jirasak/*.jpg'):
#         c+=1
#         filename = filename.split("\\")[1]
#         if filename == "20161129163859_026.jpg":
#             print("=====================================================================")
#             print(str(filename)+" "+str(c)+" : "+str(pre_process_ans("image/From_T_Jirasak/", "image/From_T_Jirasak/result/", filename)))