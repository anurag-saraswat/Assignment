
/*

Implementing the Midpoint Line Algorithm (using only integer operations) to draw a line from the point (x0, y0) to (x1, y1),


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
	gluOrtho2D (10.0, 510.0, 30.0, 530.0);


}

void drawLine(int x0 , int y0 , int x1 , int y1) {


	int dx = x1 - x0;
	int dy = y1 - y0;


	glBegin (GL_POINTS);

	GLint p = x0, q = y0;

	glVertex2i(p, q);
	glVertex2i(x1, y1);

	if (dx == 0) {

		// drawing vertical line

		for (int i = y0; i <= y1; i++) {

			GLint p = x0, q = i;
			glVertex2i(p, q);

		}
		glEnd ( );

		glFlush ( );

		return ;

	}


	if ((dx > 0) and (dy < 0) and (dx < -dy) ) {

		//for slope less than -1


		int d = 2 * dx - dy;
		int x = x0;
		int y = y0;

		while (y >= y1) {
			if (d <= 0) {
				y -= 1;
				d = d + 2 * dx;
			}
			else {
				y -= 1;
				x += 1;
				d = d + 2 * dx - 2 * dy;
			}
			p = x , q = y;
			glVertex2i(p, q);

		}

		glEnd ( );

		glFlush ( );

		return;

	}

	if ((dx > 0) and (dy < 0) and (dx >= -dy) ) {

		//for slope greater than -1 and less than 0

		int d = 2 * dy - dx;
		int x = x1;
		int y = y1;

		while (x >= x0) {
			if (d >= 0) {
				d = d + 2 * dy;
				x -= 1;

			}
			else {
				d = d + 2 * dy - 2 * dx;
				y += 1;
				x -= 1;

			}
			p = x , q = y;
			glVertex2i(p, q);
		}

		glEnd ( );

		glFlush ( );

		return;

	}


	if (dy <= dx) {
		//if slope is less than 1
		int d = 2 * dy - dx;
		int x = x0;
		int y = y0;

		while (x <= x1) {
			if (d <= 0) {
				x += 1;
				d = d + 2 * dy;
			}
			else {
				y += 1;
				x += 1;
				d = d + 2 * dy - 2 * dx;
			}
			p = x , q = y;
			glVertex2i(p, q);

		}
	}

	if (dy > dx) {

		// if slope is greater than 1

		int d = 2 * dx - dy;
		int x = x0;
		int y = y0;

		while (y <= y1) {
			if (d <= 0) {
				y += 1;
				d = d + 2 * dx;
			}
			else {
				y += 1;
				x += 1;
				d = d + 2 * dx - 2 * dy;
			}
			p = x , q = y;
			glVertex2i(p, q);

		}

	}

	glEnd ( );

	glFlush ( );

}


void MidPointLine (void)
{
	glClear (GL_COLOR_BUFFER_BIT); // Clear display window.
	glColor3f (0.0, 0.4, 0.2);



	int x0 = 50 , y0 = 200 , x1 = 200 , y1 = 50;

	if (x0 > x1) {
		drawLine(x1, y1, x0, y0);
	}
	else {
		drawLine(x0, y0, x1, y1);

	}

	x0 = 100 , y0 = 50 , x1 = 100 , y1 = 200;

	if (x0 > x1) {
		drawLine(x1, y1, x0, y0);
	}
	else {
		drawLine(x0, y0, x1, y1);

	}


	x0 = 50 , y0 = 50 , x1 = 250 , y1 = 150;

	if (x0 > x1) {
		drawLine(x1, y1, x0, y0);
	}
	else {
		drawLine(x0, y0, x1, y1);

	}

	x0 = 50 , y0 = 50 , x1 = 150 , y1 = 150;

	if (x0 > x1) {
		drawLine(x1, y1, x0, y0);
	}
	else {
		drawLine(x0, y0, x1, y1);

	}

	x0 = 50 , y0 = 50 , x1 = 150 , y1 = 250;

	if (x0 > x1) {
		drawLine(x1, y1, x0, y0);
	}
	else {
		drawLine(x0, y0, x1, y1);

	}


}

int main (int argc, char** argv)
{
	glutInit (&argc, argv);
	glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB);
	glutInitWindowPosition (10, 30);
	glutInitWindowSize (500, 500);
	glutCreateWindow ("CSL7450: Mid Point Line Drawing Algorithm Using Integer Operation");
	init ( ); 	glutDisplayFunc (MidPointLine);
	glutMainLoop ( );
}