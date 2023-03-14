def iou(bbox1: list, bbox2: list) -> float:
    # Расчет координат основной фигуры и фигуры, которая наложена
    main_up = bbox1[0]
    main_right = bbox1[2] + bbox1[3]
    main_down = bbox1[0] + bbox1[1]
    main_left = bbox1[2]

    overlay_up = bbox2[0]
    overlay_right = bbox2[2] + bbox2[3]
    overlay_down = bbox2[0] + bbox2[1]
    overlay_left = bbox2[2]

    # Отбрасываем, если фигуры не налаживаются
    if main_up >= overlay_down or main_right <= overlay_left or main_down <= overlay_up or main_left >= overlay_right:
        return 0.0

    square1 = (bbox1[1] - bbox1[0]) * (bbox1[3] - bbox1[2])
    
    square2 = (bbox2[1] - bbox2[0]) * (bbox2[3] - bbox2[2])

    union_square = (min(main_right, overlay_right) - max(main_left, overlay_left)) * (min(main_down, overlay_down) - max(main_up, overlay_up))

    return union_square / (square1 + square2 - union_square)

# --------- main code ---------

bbox1 = [0, 10, 0, 10] # номер строки, кол-во строк, номер столбца, кол-во столбцов
bbox2 = [0, 10, 1, 10]
bbox3 = [20, 30, 20, 30]
bbox4 = [5, 15, 5, 15]

assert(iou([0, 10, 0, 10], [10, 2, 0, 10]) == 0.0)  # Проверка, что фигура, которая за границами выдает 0.0
assert iou(bbox1, bbox1) == 1.0
assert iou(bbox1, bbox2) == 0.9
assert iou(bbox1, bbox3) == 0.0
assert round(iou(bbox1, bbox4), 2) == 0.14