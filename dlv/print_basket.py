#
# dlv
#
from rateslib import BondFuture, FixedRateBond, dt

def main():
    # cusip: 9128286Y1 - 3yr note
    ust9128286Y1 = FixedRateBond(
        effective=dt(2019,6,15),
        termination=dt(2022,6,15),
        fixed_rate=1 + (3/4),
        spec='ust',
        calc_mode='ust_31Bii',
    )

    # cusip: 912828XW5 - 5yr note
    ust912828XW5 = FixedRateBond(
        effective=dt(2017,6,30),
        termination=dt(2022,6,30),
        fixed_rate=1 + (3/4),
        spec='ust'
    )

    # cusip: 9128287C8 - 3yr note
    ust9128287C8 = FixedRateBond(
        effective=dt(2019,7,15),
        termination=dt(2022,7,15),
        fixed_rate=1.750,
        spec='ust'
    )

    # cusip:  9128282P4 - 5yr note
    ust9128282P4 = FixedRateBond(
        effective=dt(2017,7,31),
        termination=dt(2022,7,31),
        fixed_rate=1.875,
        spec='ust'
    )

    # cusip: 912828YA2 - 3yr note
    ust912828YA2 = FixedRateBond(
        effective=dt(2019,8,15),
        termination=dt(2022,8,15),
        fixed_rate=1.5,
        spec='ust'
    )

    # cusip: 912828YA2
    ust9128282S8 = FixedRateBond(
        effective=dt(2017,8,31),
        termination=dt(2022,8,31),
        fixed_rate=1 + (5/8),
        spec='ust'
    )

    # cusip: 912828YF1
    ust912828YF1 = FixedRateBond(
        effective=dt(2019, 9, 16),
        termination=dt(2022, 9, 15),
        fixed_rate=1.5,
        spec='ust'
    )

    # cusip: 9128282W9 - 5yr note - first payment: 2018-03-31 --> special
    ust9128282W9 = FixedRateBond(
        effective=dt(2017, 10, 2),
        termination=dt(2022, 9, 30),
        fixed_rate=1.875,
        spec='ust',
    )

    deliverableBasket = {
        '9128286Y1': (ust9128286Y1, 103 + (3/32)),
        '912828XW5': (ust912828XW5, 103 + (4+(1/2))/32),
        '9128287C8': (ust9128287C8, 103 + (6+(1/4))/32),
        '9128282P4': (ust9128282P4, 103 + (16+(7/8))/32),
        '912828YA2': (ust912828YA2, 102 + (25+(5/8))/32),
        '9128282S8': (ust9128282S8, 103 + (3+(5/8))/32),
        '912828YF1': (ust912828YF1, 102 + (29+(1/2))/32),
        '9128282W9': (ust9128282W9, 103 + (25+(7/8))/32),
    }

    usbf = BondFuture(
        coupon=6.0,
        delivery=(dt(2020,9,1), dt(2020,10,5)),
        # basket=[ust912828YF1, ust9128282W9, ust9128282S8, ust912828YA2, ust9128282P4, ust9128287C8, ust912828XW5, ust9128286Y1],  # type: ignore
        basket=[t[0] for t in deliverableBasket.values()], # type: ignore
        calc_mode='ust_short',
    )

    df = usbf.dlv(
        future_price=110 + ((11+3/8)/32),
        prices=[t[1] for t in deliverableBasket.values()],
        repo_rate=0.172,
        settlement=dt(2020,6,23),
        delivery=dt(2020,10,5),
        convention='Act360',
    )

    df['Gross Basis'] *= 32
    df['Net Basis'] *= 32
    print(df)

if __name__ == "__main__":
    main()