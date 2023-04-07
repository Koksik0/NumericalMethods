#include <stdio.h>
#include <math.h>
#include <stdlib.h>
int main()
{
    float h = 0.9;
    float x = 0.2;
    float blad = 0.0;
    float przyblizonaPochodna = 0.0;
    FILE *fp;
    fp=fopen("NUM1aFloat.txt", "w");
    FILE *przyblizenie;
    przyblizenie=fopen("przyblizonaPochodnaNUM1aFloat.txt", "w");
    for(int y = 0; y<1000000;y++)
    {
        przyblizonaPochodna = ((sin(x+h) - sin(x))/h);
        fprintf (przyblizenie, "%1.15f %1.15f\n", h, przyblizonaPochodna);
        blad = (((sin(x + h) - sin(x))/h) - cos(x));
        if(blad<0)
        {
            fprintf (fp, "%1.15f %1.15f\n", h, -blad);
        }
        else
        {
            fprintf (fp, "%1.15f %1.15f\n", h, blad);
        }
        h*=0.999;
    }
    fclose (fp);
    fclose (przyblizenie);
    return 0;
}