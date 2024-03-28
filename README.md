# deliverybasket

Prints a basket of deliverable treasuries for a given future like the dlv function of the bloomberg terminal does. To print the eligible treasuries for the 2yr future contract with the current price tag of 110'113 and a repo rate of 0.172 for the date of 06/22/2020 and the last delivery day of 10/05/2020 the future put the following in the command line:

```console
foo@bar in ~: ./dlv.sh print --future=tuu0 --price=110-113 --repo-rate=0.172 --trade=2020-06-22 --ldd=2020-10-05
```
This results in the following output:

```console
Last delivery day: 2020-10-03 00:00:00
Future price: 110.35546875
Calculation mode: ust_short

                Bond       Price       YTM  C.Factor  Gross Basis  Implied Repo  Actual Repo  Net Basis      CUSIP
3  1.750% 15-06-2022  103.093750  0.184604    0.9303    13.761837      0.211582        0.172  -0.373724  9128286Y1
5  1.750% 30-06-2022  103.140625  0.192876    0.9303    15.261837      0.052693        0.172   1.126955  912828XW5
4  1.750% 15-07-2022  103.195312  0.197331    0.9272    27.959100     -1.295145        0.172  13.873135  9128287C8
0  1.875% 31-07-2022  103.527344  0.196675    0.9294    30.815075     -1.469745        0.172  15.584450  9128282P4
6  1.500% 15-08-2022  102.800781  0.192944    0.9196    42.172550     -3.039616        0.172  30.282145  912828YA2
1  1.625% 31-08-2022  103.113281  0.199688    0.9219    44.050387     -3.108868        0.172  31.046362  9128282S8
7  1.500% 15-09-2022  102.921875  0.186933    0.9164    57.347950     -4.643753        0.172  45.499312  912828YF1
2  1.875% 30-09-2022  103.808594  0.193932    0.9233    61.356462     -4.669863        0.172  46.195918  9128282W9
```

which should respond to same result as the dlv-function of the bloomberg terminal :)


