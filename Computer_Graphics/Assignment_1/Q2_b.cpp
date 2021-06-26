
/*

Extend the incremental line drawing to draw a triangle.

Here drawLine function drawline using incremental line algo.

Approach Used:

let are the vertices of triangle.

To raster triangle using increment line algorithm.
- First draw Boundary of Triangle.
- Then , Choose one side as base.
- Choose point x on base then corresponding to that x ,find y on base and on the other side.
- Then join the two points i.e point on base and other side.
- We choose x on base in two parts. First we will choose all x on base which are less than the x of third remaining vertex.
- Second, we choose x on base from x of third vertex to the end of base.
- In this way we eventually rasterize whole left and right triangle.


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

void drawLine(int x0 , int y0 , int x1, int y1) {


	glColor3f (0.0, 0.4, 0.2);

	glBegin (GL_POINTS);

	float dy = (y1 - y0);
	float dx = (x1 - x0);



	// Drawing vertical line
	if (dx == 0) {
		for (int i = y0 ; i <= y1; i++) {
			GLint a = x0, b = i;
			glVertex2i(a, b);
		}

		glEnd ( );
		glFlush ( );

		return;
	}

	float m = dy / dx;

	if (m >= 0) {

		float y = y0;
		for (int i = x0; i <= x1; i++) {

			GLint a = i, b = int(y);
			glVertex2i(a, b);

			y = y + m ;

		}

	}
	else {
		float x = x0;

		for (int i = y0; i <= y1; i++) {

			GLint a = int(x), b = i;
			glVertex2i(a, b);

			x = x + (1 / m) ;

		}

	}



	glEnd ( );
	glFlush ( );

}

void TriangleRaster (void)
{
	glClear (GL_COLOR_BUFFER_BIT); // Clear display window.
	glColor3f (0.0, 0.4, 0.2);


	int x0 = 50 , x1 = 0 , x2 = 150;
	int y0 = 150 , y1 = 0 , y2 = 10;

	drawLine(x1, y1, x2, y2);
	drawLine(x1, y1, x0, y0);
	drawLine(x2, y2, x0, y0);

	// Finding Slope of each line

	float m1 = float(y2 - y1) / float(x2 - x1);
	float m2 = float(y0 - y1) / float(x0 - x1);
	float m3 = float(y2 - y0) / float(x2 - x0);

	for (int i = x1; i <= x0; i++) {

		int x_0 = i;
		int y_0 = int(m1 * (x_0 - x1) + y1);

		int x_1 = i;
		int y_1 = int(m2 * (x_1 - x1) + y1);
		drawLine(x_0, y_0, x_1, y_1);

	}
	for (int i = x0; i <= x2; i++) {

		int x_0 = i;

		// Finding y using equation of line.
		// y-y1 = m(x-x1)
		int y_0 = int(m1 * (x_0 - x1) + y1);

		int x_1 = i;
		// Finding y using equation of line.
		int y_1 = int(m3 * (x_1 - x2) + y2);
		drawLine(x_0, y_0, x_1, y_1);

	}

}

int main (int argc, char** argv)
{
	glutInit (&argc, argv);
	glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB);
	glutInitWindowPosition (10, 30);
	glutInitWindowSize (500, 500);
	glutCreateWindow ("CSL7450: Extend the incremental line drawing to draw a triangle.");
	init ( );
	glutDisplayFunc (TriangleRaster);
	glutMainLoop ( );

}