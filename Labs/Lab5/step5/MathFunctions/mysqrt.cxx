#include <stdio.h>
#include "MathFunctions.h"
#include "TutorialConfig.h"

#include "Table.h"

#include <math.h>

double mysqrt(double x)
{
  if (x <= 0)
    {
    return 0;
    }

  double result;

  double delta;

  result = x;
  if (x >= 1 && x < 10)
    {
    result = sqrtTable[static_cast<int>(x)];
    }

  int i;
  for (i = 0; i < 10; ++i)
    {
    if (result <= 0)
      {
      result = 0.1;
      }
    delta = x - (result*result);
    result = result + 0.5*delta/result;
    fprintf(stdout,"Computing sqrt of %g to be %g\n",x,result);
    }

  return result;
}
