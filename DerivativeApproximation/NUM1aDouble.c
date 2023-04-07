#include <stdio.h>
#include <math.h>
#include <stdlib.h>
int main()
{
    double h = 0.9;
    double x = 0.2000000000000000;
    double blad = 0.0;
    float przyblizonaPochodna = 0.0;

    FILE *fp;
    fp=fopen("NUM1aDouble.txt", "w");
    FILE *przyblizenie;
    przyblizenie=fopen("przyblizonaPochodnaNUM1aDouble.txt", "w");
    for(int y = 0; y<1000000;y++)
    {
        przyblizonaPochodna = (sin(x+h) - sin(x))/h;
        fprintf (przyblizenie, "%1.30f %1.30f\n", h, przyblizonaPochodna);
        blad = (((sin(x + h) - sin(x))/h) - cos(x));
        if(blad<0)
        {
            fprintf (fp, "%1.30f %1.30f\n", h, -blad);
        }
        else
        {
            fprintf (fp, "%1.30f %1.30f\n", h, blad);
        }
        h*=0.999;
    }
    fclose (fp);
    fclose (przyblizenie);
}