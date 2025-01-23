# 一个计算北京公积金贷款的小工具：
# 可以修改自己的还款周期 period 多少个月
# repay是每月还款额的遍历范围
# interest_rate为当前公积金利率
# total为待还款总额
# 目的是计算某一个月还款额下，需要的总利息等数据

period = 300
repay = [x * 10 for x in range(150, 300)]
interest_rate = 0.0285 / 12
TOTAL = 1200000


def gongjijin():
    for try_repay in repay:
        total = TOTAL
        now_total = total
        total_interest = 0
        total_principal = 0
        complete_after_end = 0
        complete_before_end = 0
        last_month_principle = 0
        repay_month = period
        for i in range(period):
            now_interest = now_total * interest_rate
            total_interest += now_interest
            now_total -= (try_repay - now_interest)
            total_principal += (try_repay - now_interest)
            if i == max(range(period)):
                if now_total < total:
                    complete_after_end = 1
                    last_month_principle = total - total_principal
            if total_principal >= total:
                complete_before_end = 1
                repay_month = i + 1
                break

        print(f'每月还款 {try_repay}, 总利息 {round(total_interest)}, 总本金 {round(total_principal)}, '
              f'最后一月需还本金 {round(last_month_principle)}, 最后一月利息 {round(now_interest)}, '
              f'提前还完 {complete_before_end}, 还款月数 {repay_month}')


if __name__ == '__main__':
    gongjijin()
