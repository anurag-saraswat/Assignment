/*

Implement the bounding box based algorithm to draw a triangle with vertices (x0, y0), (x1, y1), (x2, y2).

 */


#include <GL/glut.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include<iostream>

using namespace std;

void init (void)
{
	glClearColor (1.0, 1.0, 1.0, 0.0);
	glMatrixMode (GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D (-250.0, 250.0, -250.0, 250.0);
}

int findmin(int a , int b, int c) {
	a = min(a, b);
	return min(a, c);
}
int findmax(int a , int b, int c) {
	a = max(a, b);
	return max(a, c);
}

void TriangleRaster (void)
{
	glClear (GL_COLOR_BUFFER_BIT);
	glColor3f (0.0, 0.4, 0.2);


	int x0 = 50 , x1 = 0 , x2 = 150;
	int y0 = 150 , y1 = 0 , y2 = 0;

	int dx0 = x1 - x0 , dx1 = x2 - x1 , dx2 = x0 - x2;
	int dy0 = y1 - y0 , dy1 = y2 - y1 , dy2 = y0 - y2;

	int x_min = findmin(x0 , x1 , x2);
	int y_min = findmin(y0 , y1 , y2);

	int x_max = findmax(x0 , x1 , x2);
	int y_max = findmax(y0 , y1 , y2);

	int q = x_max - x_min;

	int f0 = (x_min - x0) * dy0 - (y_max - y0) * dx0;
	int f1 = (x_min - x1) * dy1 - (y_max - y1) * dx1;
	int f2 = (x_min - x2) * dy2 - (y_max - y2) * dx2;

	glBegin (GL_POINTS);

	for (int i = y_max; i >= y_min; i--) {
		for (int j = x_min; j <= x_max; j++) {

			if ((f0 < 0) and (f1 < 0) and (f2 < 0)) {
				GLint a = j, b = i;
				glVertex2i(a, b);

			}

			f0 = f0 + dy0;
			f1 = f1 + dy1;
			f2 = f2 + dy2;

		}

		f0 = f0 - q * dy0;
		f0 = f0 + dx0;

		f1 = f1 - q * dy1;
		f1 = f1 + dx1;

		f2 = f2 - q * dy2;
		f2 = f2 + dx2;
	}
	glEnd ( );

	glFlush ( );



}
int main (int argc, char** argv)
{
	glutInit (&argc, argv);
	glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB);
	glutInitWindowPosition (10, 30);
	glutInitWindowSize (500, 500);
	glutCreateWindow ("CSL7450: Bounding Box Based Triangle Rasterization Algorithm");
	init ( );
	glutDisplayFunc (TriangleRaster);
	glutMainLoop ( );
}