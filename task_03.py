#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""Loan calculation."""


NAME = raw_input('What is your name? ')
PRINCIPAL = raw_input('How much are you borrowing? )
PRINCIPAL = int(PRINCIPAL)
TERM = raw_input('For how many years are you borrowing? )
TERM = int(TERM)
QUALIFICATION = ('Are  you prequalified for this? ')
YES = ('y')

NO = ('n')

TOTAL = A=P(1+\frac{r}{n})^{nt}
        \text{Where}\\
&A \text{ is the total amount accumulated, with interest, over the
duration of the loan}\\
&P \text{ is the principal amount (the initial amount borrowed)}\\
&r \text{ is the annual rate of interest represented as a decimal}\\
&n \text{ is the number of times the interest is compounded each
year}\\
&t \text{ is the number of years for which } P \text{ is borrowed}\\
