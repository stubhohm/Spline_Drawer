
def bezier_point(segment, t):
    start = segment.start_point
    start_control = segment.start_control_point
    end = segment.end_point
    end_control = segment.end_control_point
    # De Casteljau's algorithm
    p1 = int((1 - t) * start[0] + t * start_control[0]), int((1 - t) * start[1] + t * start_control[1])
    p2 = int((1 - t) * start_control[0] + t * end_control[0]), int((1 - t) * start_control[1] + t * end_control[1])
    p3 = int((1 - t) * end_control[0] + t * end[0]) , int((1 - t) * end_control[1] + t * end[1])

    p4 = int((1 - t) * p1[0] + t * p2[0]), int((1 - t) * p1[1] + t * p2[1])
    p5 = int((1 - t) * p2[0] + t * p3[0]), int((1 - t) * p2[1] + t * p3[1])

    p6 = int((1 - t) * p4[0] + t * p5[0]), int((1 - t) * p4[1] + t * p5[1])

    return p6



def main():
    print('bezier curve')

if __name__ == '__main__':
    main()
    print(
        'this main only runs if this file is ran, not if another program executes it: bezier curve'
    )
