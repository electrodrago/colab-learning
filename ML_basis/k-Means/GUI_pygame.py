import numpy as np
import pygame
from random import randint
import math
from sklearn.cluster import KMeans


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


# Bắt đầu bằng init chứ k init sao có nó
# Căn chỉnh độ rộng của cái màn hình hiểu thị
# Đặt tên cho cái chương trình này
pygame.init()
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("K-means visualization")

# Trạng thái running để tiếp tục chạy chương trình
# Tạo mới clock kiểm soát quá trình chạy chương trình
# Màu nền dạng RGB (214, 214, 214) -> màu xám xám
# Màu nên cho hình chữ nhật tương tác, BLACK là hình chữ nhật nằm sau
# Hình chữ nhật (BACKGROUND_PANEL) đè lên nó có màu hồng cánh sen (232, 211, 227)
running = True
clock = pygame.time.Clock()
BACKGROUND = (214, 214, 214)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 191, 255)
YELLOW = (173, 255, 47)
BACKGROUND_PANEL = (232, 211, 227)
COLOUR = [(255, 0, 0), 	(0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255), (0, 128, 128)]

# Tạo font cho chữ trong chương trình
font = pygame.font.SysFont('sans', 38)
font1 = pygame.font.SysFont('sans', 14)
dau_cong = font.render('+', True, WHITE)
dau_tru = font.render('-', True, WHITE)
nut_run = font.render("Run", True, WHITE)
nut_random = font.render("Random", True, WHITE)
nut_algorithm = font.render("Algorithm", True, WHITE)
nut_reset = font.render("Reset", True, WHITE)

# Số điểm phân loại K
# Error hiển thị lên pygame
# Các điểm dữ liệu mình đã chấm lên
K = 0
error = 0
points = []
clusters = []
labels = []

while running:
    # Nháy màn hình 60 lần 1 giây (fps)
    clock.tick(60)
    screen.fill(BACKGROUND)

    # Vẽ cái panel tương tác
    pygame.draw.rect(screen, BLACK, (50, 50, 600, 400))
    pygame.draw.rect(screen, BACKGROUND_PANEL, (55, 55, 590, 390))

    # Chữ K
    text_k = font.render("K = " + str(K), True, BLACK)
    screen.blit(text_k, (790, 50))

    # Vẽ mấy cái button
    pygame.draw.ellipse(screen, BLACK, (700, 50, 50, 50))
    screen.blit(dau_cong, (715, 50))

    pygame.draw.ellipse(screen, BLACK, (900, 50, 50, 50))
    screen.blit(dau_tru, (920, 50))

    pygame.draw.rect(screen, BLACK, (700, 120, 250, 50))
    screen.blit(nut_run, (790, 120))

    pygame.draw.rect(screen, BLACK, (700, 190, 250, 50))
    screen.blit(nut_random, (780, 190))

    # screen.blit(font.render("Error = " + str(error), True, BLACK), (720, 260))

    pygame.draw.rect(screen, BLACK, (700, 330, 250, 50))
    screen.blit(nut_algorithm, (780, 330))

    pygame.draw.rect(screen, BLACK, (700, 400, 250, 50))
    screen.blit(nut_reset, (780, 400))

    # Vị trí con trỏ chuột
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Vẽ vị trí con trỏ chuột khi con trỏ chuột lia vào vùng cấm
    if 55 < mouse_x < 645 and 55 < mouse_y < 445:
        text_mouse = font1.render("(" + str(mouse_x - 55) + "," + str(mouse_y - 55) + ")", True, BLACK)
        screen.blit(text_mouse, (mouse_x + 10, mouse_y + 10))

    # Các event xuất hiện trong chương trình
    for event in pygame.event.get():
        # Quit ra khỏi chương trình -> running = false
        if event.type == pygame.QUIT:
            running = False
        # Con trỏ chuột được bấm xuống
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Bấm vào trong vùng cấm
            if 55 < mouse_x < 645 and 55 < mouse_y < 445:
                labels = []
                points.append([mouse_x - 55, mouse_y - 55])

            # Bấm 7749 các loại nút
            if 700 < mouse_x < 750 and 50 < mouse_y < 100:
                print('Press +')
                if K < 7:
                    K += 1
            if 900 < mouse_x < 950 and 50 < mouse_y < 100:
                print("Press -")
                if K > 0:
                    K -= 1
            if 700 < mouse_x < 950 and 120 < mouse_y < 170:
                # Tính khoảng cách từ 1 điểm đến mỗi cluster -> tìm ra khoảng cách bé nhất
                # Tìm ra cái label tại index nhỏ nhất ấy -> đổi màu
                # Đưa label về rỗng mỗi lần mình chạy lại
                labels = []
                if not np.array_equal(clusters, []):
                    for p in points:
                        distances_to_cluster = []
                        for c in clusters:
                            distances_to_cluster.append(distance(p, c))
                        min_dis = min(distances_to_cluster)
                        label = distances_to_cluster.index(min_dis)
                        labels.append(label)
                    # Đưa tâm cluster vào giữa cái group
                    for i in range(K):
                        sum_x = 0
                        sum_y = 0
                        counter = 0
                        for j in range(len(points)):
                            if labels[j] == i:
                                counter += 1
                                sum_x += points[j][0]
                                sum_y += points[j][1]
                        if counter != 0:
                            clusters[i][0] = int(sum_x / counter)
                            clusters[i][1] = int(sum_y / counter)
                    error = 0
                    for i in range(len(points)):
                        error += distance(points[i], clusters[labels[i]])
                print('Press Run')
            if 700 < mouse_x < 950 and 190 < mouse_y < 240:
                labels = []
                clusters = []
                for i in range(K):
                    clusters.append([randint(0, 590), randint(0, 390)])
                print('Press Random')
            if 700 < mouse_x < 950 and 330 < mouse_y < 380:
                if K != 0:
                    kmean = KMeans(n_clusters=K, ).fit(points)
                    clusters = kmean.cluster_centers_
                    labels = kmean.predict(points)
                    error = 0
                    for i in range(len(points)):
                        error += distance(points[i], clusters[labels[i]])
                print('Press Algorithm')
            if 700 < mouse_x < 950 and 400 < mouse_y < 450:
                K = 0
                error = 0
                points = []
                clusters = []
                labels = []
                print('Press Reset')

    # Vẽ mấy cái điểm mình đã random ra
    for i in range(len(clusters)):
        # pygame.draw.circle(screen, BLACK, (clusters[i][0] + 55, clusters[i][1] + 55), 6)
        pygame.draw.circle(screen, COLOUR[i], (clusters[i][0] + 55, clusters[i][1] + 55), 7)

    # Câu lệnh giúp mấy điểm mà mình chấm chấm lên màn hình được hiển thị
    for i in range(len(points)):
        pygame.draw.circle(screen, BLACK, (points[i][0] + 55, points[i][1] + 55), 6)
        # Nều chưa có labels thì vẽ màu trắng bình thường, k thì vẽ màu
        if np.array_equal(labels, []):
            pygame.draw.circle(screen, WHITE, (points[i][0] + 55, points[i][1] + 55), 5)
        else:
            pygame.draw.circle(screen, COLOUR[labels[i]], (points[i][0] + 55, points[i][1] + 55), 5)

    # Tính lỗi và hiển thị
    # if not clusters and not labels:
    #     for i in range(len(points)):
    #         error += distance(points[i], clusters[labels[i]])
    screen.blit(font.render("Error = " + str(int(error)), True, BLACK), (720, 260))
    pygame.display.flip()

# Xóa những cái mà pygame đang sử dụng
pygame.quit()
