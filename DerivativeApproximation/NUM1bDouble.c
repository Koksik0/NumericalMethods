#include <stdio.h>
#include <math.h>
#include <stdlib.h>
int main()
{
    double h = 0.0000000000000001;
    double x = 0.2;
    double blad = 0.0;
    float przyblizonaPochodna = 0.0;

    FILE *fp;
    fp=fopen("NUM1bDouble.txt", "w");
    FILE *przyblizenie;
    przyblizenie=fopen("przyblizonaPochodnaNUM1bDouble.txt", "w");
    for(int y = 0; y<1000;y++)
    {
        przyblizonaPochodna = (sin(x+h) - sin(x-h))/(2*h);
        fprintf (przyblizenie, "%1.30f %1.30f\n", h, przyblizonaPochodna);
        blad = (((sin(x + h) - sin(x-h))/(2*h)) - cos(x));
        if(blad<0)
        {
            fprintf (fp, "%1.30f %1.30f\n", h, -blad);
        }
        else
        {
            fprintf (fp, "%1.30f %1.30f\n", h, blad);
        }
        h*=1.1;
    }
    fclose (fp);
    fclose (przyblizenie);
    return 0;
}