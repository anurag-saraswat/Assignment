#include <GL/glut.h> // (or others, depending on the system in use)
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

void init (void)
{
    glClearColor (1.0, 1.0, 1.0, 0.0); // display window color .
    glMatrixMode (GL_PROJECTION); // projection parameters.
    glLoadIdentity();
    gluOrtho2D (0.0, 500.0, 0.0, 500.0);
}

void lineIUA (void)
{
    glClear (GL_COLOR_BUFFER_BIT); // Clear display window.
    glColor3f (0.0, 0.4, 0.2);

    int x0 = 10;
    int y0 = 10;
    int x1 = 500;
    int y1 = 300;
    float dx = x1 - x0;
    float dy = y1 - y0;
    float m = dy / dx;
    GLint x = x0, y = y0;

    glBegin (GL_POINTS);
    glVertex2i(x, y);
    glEnd();

    float yf = float(y0);

    glBegin (GL_POINTS);
    for (x = 11; x <= 500; x++) {
        yf = yf + m;
        y = int(yf + 0.5);
        glVertex2i (x, y);
    }
    glEnd ( );

    glFlush ( );
}
int main (int argc, char** argv)
{
    glutInit (&argc, argv); // Initialize GLUT.
    glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB); // Set display mode.
    glutInitWindowPosition (20, 20); // Set top-left display-window position.
    glutInitWindowSize (500, 500); // Set display-window width and height.
    glutCreateWindow ("CSL7450: Incremental Line Drawing"); // Create display window.
    init ( ); // Execute initialization procedure.
    glutDisplayFunc (lineIUA); // Send graphics to display window.
    glutMainLoop ( ); // Display everything and wait.
}