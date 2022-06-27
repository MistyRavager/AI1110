#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

int  main(void) //main function begins
{
//making data
uniform("../dat_files/uni.dat", 1000000);
gaussian("../dat_files/gau.dat", 1000000);
uniform_sq("../dat_files/uni_sq.dat",1000000);
gaussian_sq("../dat_files/gau_sq.dat",1000000);

//uniform
double e_u = mean("../dat_files/uni.dat");
double e_u_2 = mean("../dat_files/uni_sq.dat");
double var = e_u_2 - e_u*e_u;
//Mean of uniform
printf("e_u_2 = %lf\n",e_u_2);
printf("mean = %lf\n",e_u);
printf("variance = %lf\n",var);

//gaussian
double e_x = mean("../dat_files/gau.dat");
double e_x_2 = mean("../dat_files/gau_sq.dat");
double var2 = e_x_2 - e_x*e_x;

//mean of gaussian
printf("mean2 = %lf\n",e_x);
printf("variance2 = %lf\n",var2);

//V = -2*ln(1-U)
V("V.dat",1000000);


return 0;
}

