import string
import random


def coupon_creator(digit):
    #优惠券生成器，digit是优惠码长度
    coupon = ''
    for word in range(digit):
        coupon += random.choice(string.ascii_uppercase + string.digits)
    return coupon


def two_hundred_coupons():
    data = ''
    count = 1
    for count in range(200):
        digit = 12
        #因为digit是一个函数内的数值，并不需要全局定义
        count += 1
        data += 'coupon no.' + str(count) + '  ' + coupon_creator(digit) + '\n'

    return data
    #注意，这里的data是一个类似于数组的形式


coupondata = open('coupondata.txt', 'w')
coupondata.write(two_hundred_coupons())
#two_hundred_coupons()返回了一个数组
coupondata.close()