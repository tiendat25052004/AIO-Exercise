def check_type(a):
    if type(a) is not int:
        return False
    return True


def exercise1(tp, fp, fn):
    if not check_type(tp):
        print('tp must be an integer')
        return
    if not check_type(fp):
        print('fp must be an integer')
        return
    if not check_type(fp):
        print('fp must be an integer')
        return
    if ((tp <= 0) or (fp <= 0) or (fn <= 0)):
        print('tp, fp, fn must be greater than 0')
        return
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = 2 * precision * recall / (precision + recall)
    print("Precision: ", precision)
    print("Recall: ", recall)
    print("F1: ", f1)
