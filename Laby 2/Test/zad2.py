def bmr(w,h,y,g):
   if g == 'm':
       BMR = 66.5 + (13.75 * w) + (5.003 * h) - (6.755 * y)
       return(round(BMR,2))
   if g == 'f':
       BMR = 655 + (9.563 * w) + (1.850 * h) - (4.676 * y)
       return(round(BMR,2))
