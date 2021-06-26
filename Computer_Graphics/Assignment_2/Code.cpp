
#include <GL/glut.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include<iostream>
#include <fstream>
#include <vector>
#include <string.h>

using namespace std;



void init (void)
{
	glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
	glClearDepth(1.0f);
	glEnable(GL_DEPTH_TEST);
	glDepthFunc(GL_LEQUAL);
	glShadeModel(GL_SMOOTH);
	glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST);
}



vector<string> splitString(string s) {
	vector<string> outp;
	string temp = "";
	for (int i = 0; i < s.length(); i++) {
		if (s[i] == ' ') {
			outp.push_back(temp);
			temp = "";
		}
		else {
			temp += s[i];
		}
	}
	if (temp != "") {
		outp.push_back(temp);
	}
	return outp;
}


void WolfRasterization (void)
{

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT); 
	glMatrixMode(GL_MODELVIEW);    

	glLoadIdentity();               
	glTranslatef(0.0f, 0.0f, -10.0f); 
	glScalef(0.3f, 0.3f, 0.3f);

	////////////////////////////////////////////////////////////////////////////////////
	//Reading Data from File

	string myStr;
	ifstream MyReadFile("./PA2_Models/wolf02.off");

	getline (MyReadFile, myStr);
	getline (MyReadFile, myStr);


	vector<string> temp = splitString(myStr);

	int num_vertices = stoi(temp[0]);
	int num_triangles = stoi(temp[1]);

	float vertex[num_vertices][3];
	int triangle[num_triangles][3];


	for (int i = 0; i < num_vertices; i++) {
		getline (MyReadFile, myStr);
		temp = splitString(myStr);

		vertex[i][0] = stof(temp[0]);
		vertex[i][1] = stof(temp[1]);
		vertex[i][2] = stof(temp[2]);

	}

	for (int i = 0; i < num_triangles; i++) {

		getline (MyReadFile, myStr);
		temp = splitString(myStr);

		triangle[i][0] = stoi(temp[1]);
		triangle[i][1] = stoi(temp[2]);
		triangle[i][2] = stoi(temp[3]);

	}

	MyReadFile.close();


	/////////////////////////////////////////////////////////////////////////////////////////
	///       Transforming the object w.r.t. the camera coordinate system.
	float cam_x = 10;
	float cam_y = 10;
	float cam_z = 10;

	for (int i = 0; i < num_vertices; i++) {
		getline (MyReadFile, myStr);
		temp = splitString(myStr);

		vertex[i][0] -= cam_x ;
		vertex[i][1] -= cam_y ;
		vertex[i][2] -= cam_z ;
	}

	//////////////////////////////////////////////////////////////////////////////////////////
	///    Find oriented normal for each triangle.
	///     U = p2 - p1
	///     V = p3 - p1
	///     N = U X V
	///     Nx = UyVz - UzVy
	///     Ny = UzVx - UxVz
	///     Nz = UxVy - UyVx
	///


	float normal[num_triangles][3];

	for (int i = 0; i < num_triangles; i++) {

		float p1_x = vertex[triangle[i][0]][0];
		float p1_y = vertex[triangle[i][0]][1];
		float p1_z = vertex[triangle[i][0]][2];

		float p2_x = vertex[triangle[i][1]][0];
		float p2_y = vertex[triangle[i][1]][1];
		float p2_z = vertex[triangle[i][1]][2];

		float p3_x = vertex[triangle[i][2]][0];
		float p3_y = vertex[triangle[i][2]][1];
		float p3_z = vertex[triangle[i][2]][2];


		float u_x = p2_x - p1_x;
		float u_y = p2_y - p1_y;
		float u_z = p2_z - p1_z;

		float v_x = p3_x - p1_x;
		float v_y = p3_y - p1_y;
		float v_z = p3_z - p1_z;

		normal[i][0] = u_y * v_z  - u_z * v_y ;
		normal[i][1] = u_z * v_x  - u_x * v_z ;
		normal[i][2] = u_x * v_y  - u_y * v_x ;

	}

/////////////////////////////////////////////////////////////////////////////////////////////////////
///         Determine the coordinates of the view frustum such that all the triangles lie in the view frustum.
///
///

	float x_min = vertex[0][0];
	float x_max = vertex[0][0];

	float y_min = vertex[0][1];
	float y_max = vertex[0][1];

	float z_min = vertex[0][2];
	float z_max = vertex[0][2];



	for (int i = 0; i < num_vertices; i++) {

		if (vertex[i][0] > x_max) x_max = vertex[i][0];
		if (vertex[i][0] < x_min) x_min = vertex[i][0];

		if (vertex[i][1] > y_max) y_max = vertex[i][1];
		if (vertex[i][1] < y_min) y_min = vertex[i][1];

		if (vertex[i][0] > z_max) z_max = vertex[i][2];
		if (vertex[i][0] < z_min) z_min = vertex[i][2];

	}

///////////////////////////////////////////////////////////////////////////////////////////
///           Applying BaackFace Culling Algo and Phong Shading


	float light_x = -70;
	float light_y = 30;
	float light_z = 60;

	cam_x = 10;
	cam_y = 10;
	cam_z = 10;

	int phong[num_triangles] = {0};
	int backFace[num_triangles] = {0};

	for (int i = 0; i < num_triangles; i++) {

		float c = light_x * normal[i][0] + light_y * normal[i][1] + light_z * normal[i][2];
		float n = cam_x * normal[i][0] + cam_y * normal[i][1] + cam_z * normal[i][2];

		if (c > 0) {
			phong[i] = 1;
		}

		if (n >= 0) {
			backFace[i] = 1;
		}

	}



//////////////////////////////////////////////////////////////////////////////////////////
///                      Triangle Rasterization
///
	glBegin(GL_TRIANGLES);

	for (int i = 0; i < num_triangles; i++) {


		if (phong[i] == 1)glColor3f(1.0f, 1.0f, 0.0f);
		else glColor3f(1.0f, 1.0f, 1.0f);

		if (backFace[i] == 1) {
			int v1 = triangle[i][0];
			int v2 = triangle[i][1];
			int v3 = triangle[i][2];
			glVertex3f(vertex[v1][0] / 10, vertex[v1][1] / 10, vertex[v1][2] / 10);
			glVertex3f(vertex[v2][0] / 10, vertex[v2][1] / 10, vertex[v2][2] / 10);
			glVertex3f(vertex[v3][0] / 10, vertex[v3][1] / 10, vertex[v3][2] / 10);
		}
	}
	glEnd();
	glutSwapBuffers();
}


//////////////////////////////////////////////////////////
///Perspective Projection

void reshape(GLsizei width, GLsizei height) {
	if (height == 0) height = 1;
	GLfloat aspect = (GLfloat)width / (GLfloat)height;
	glViewport(0, 0, width, height);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluPerspective(45.0f, aspect, 0.1f, 100.0f);
}


int main (int argc, char** argv)
{
	glutInit (&argc, argv);
	glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB);
	glutInitWindowPosition (10, 30);
	glutInitWindowSize (500, 500);
	glutCreateWindow("CSL7450: Wolf Rasterization");
	glutReshapeFunc(reshape);
	init();
	glutDisplayFunc (WolfRasterization);
	glutMainLoop();
}
