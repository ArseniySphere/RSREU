
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>
#include <float.h>
#include <iostream>

typedef struct {
    float lx;
    float ly;
    float rx;
    float ry;
    bool sq;
} Rectangle;

bool eq_num(float x, float y) {
    return fabs(x - y) < 1e-6;
}

float len_seg(float x1, float y1, float x2, float y2) {
    return fabs(x2 - x1) + fabs(y2 - y1);
}

Rectangle create_rectangle(float lx, float ly, float rx, float ry)
{
	Rectangle rec;
	rec.lx = lx;
	rec.ly = ly;
	rec.rx = rx;
	rec.ry = ry;
	
	rec.sq = (bool) eq_num(len_seg(lx, ly, rx, ly), len_seg(rx, ry, rx, ly));
	return rec;
}

void print(const Rectangle* rec)
{
    float lx = rec->lx, ly = rec->ly, rx = rec->rx, ry = rec->ry;

    printf(" (%.2f, %1.2f)\t (%.2f, %.2f)\n", lx, ly, rx, ly);
    printf(" (%.2f, %1.2f)\t (%.2f, %.2f)\n", lx, ry, rx, ry);

    if (rec->sq)
    {
        printf("[%s]\n", "Квадрат");
    }
    else
    {
        printf("[%s]\n", "Прямоугольник");
    }
}

void axial_shift(Rectangle* rec, float dx, float dy) 
{
    rec->lx += dx;
    rec->ly += dy;
    rec->rx += dx;
    rec->ry += dy;
}

void change_height_width(Rectangle* rec, float dx, float dy)
{
    rec->rx += dx;
    rec->ry += dy;
    
    rec->sq = (bool) eq_num(len_seg(rec->lx, rec->ly, rec->rx, rec->ly), len_seg(rec->rx, rec->ry, rec->rx, rec->ly));
}

void area_perim(const Rectangle* rec, float* area, float* perim)
{
	float height = len_seg(rec->lx, rec->ly, rec->rx, rec->ly);
	float width = len_seg(rec->rx, rec->ry, rec->rx, rec->ly);
	
	*area = height * width;
	*perim = (height + width) * 2;
}

Rectangle create_min(float arr[10][2], int n)
{
    Rectangle rec;
    float minx, miny = FLT_MAX;
    float maxx, maxy = FLT_MIN;
    float curx, cury;
    int j;
    for (j = 0; j < n; j++)
    {
        curx = arr[j][0];
        cury = arr[j][1];
        if (curx < minx)
            minx = curx;
        if (curx > maxx)
            maxx = curx;
        if (cury < miny)
            miny = cury;
        if (cury > maxy)
            maxy = cury;
    }
    
    rec.lx = minx;
    rec.ly = maxy;
    rec.rx = maxx;
    rec.ry = miny;
    
    rec.sq = (bool) eq_num(len_seg(minx, maxy, maxx, maxy), len_seg(maxx, miny, maxx, maxy));
    
    return rec;
}

float max(float a, float b){
    if (a > b)
        return a;
    else
        return b;
}

float min(float a, float b){
    if (a < b)
        return a;
    else
        return b;
}

Rectangle create_itrs(const Rectangle* rec1, const Rectangle* rec2, bool* exist)
{
	float x1 = rec1->lx, x2 = rec1->rx, y1 = rec1->ry, y2 = rec1->ly;
	float x3 = rec2->lx, x4 = rec2->rx, y3 = rec2->ry, y4 = rec2->ly;
	float x5 = max(x1, x3);
	float y5 = max(y1, y3);
	float x6 = min(x2, x4);
	float y6 = min(y2, y4);
	
	if (x5 > x6 || y5 > y6)
		*exist = false;
	else
		*exist = true;
	
	Rectangle rec = create_rectangle(x5, y6, x6, y5);
	return rec;
	
}

Rectangle create_cir(float x, float y, float r) {
    Rectangle rec;
    
    float half = r / sqrt(2);

    rec.lx = x - half;
    rec.ly = y + half;
    
    rec.rx = x + half;
    rec.ry = y - half;
    rec.sq = true;
    
    return rec;
}

int main() {
    bool exist = false;
    bool f = true;
    int com = 0;
    int num_points, i;
    float lx, ly, rx, ry, x, y, r;
    float dx, dy, area, perim;
    float points[10][2];
    Rectangle rec, rec_1, rec_2;
    
    while(f)
    {

        std::cout << "Введите команду:" << "\n";
        std::cout << "1. Создать прямоугольник по двум вершинам" << "\n";
        std::cout << "2. Переместить прямоугольник" << "\n";
        std::cout << "3. Изменить ширину и высоту" << "\n";
        std::cout << "4. Вычислить площадь и периметр" << "\n";
        std::cout << "5. Найти прямоугольник минимальной площади, который покрывает все точки" << "\n";
        std::cout << "6. Найти прямоугольник как пересечение двух прямоугольников" << "\n";
        std::cout << "7. Найти прямоугольник, вписанный в окружность" << "\n";
        std::cout << "8. Вывод прямоугольника" << "\n";
        std::cout << "9. Завершение работы" << "\n";
        std::cout << "Команда: ";
		std::cin >> com;

		
		switch(com)
		{
			case 1:
				do{
                    std::cout << "Введите координаты двух точек прямоугольника: " << "\n";
                    std::cin >> lx >> ly >> rx >> ry;
					if (lx < rx && ry < ly){
						break;
					}
					else{
						std::cout << "Неверные данные" << "\n";
					}
					}while(1);
					
					rec = create_rectangle(lx, ly, rx, ry);
					std::cout << "Прямоугольник создан" << "\n";
					exist = true;
                    break;
		    case 2:
				if (!exist){
                    std::cout << "Прямоугольник еще не создан" << "\n";
					break;
				}
                std::cout << "Введите значение смещения прямоугольника по оси x и y: " << "\n";
                std::cin >> dx >> dy;
				
				axial_shift(&rec, dx, dy);
                std::cout << "Прямоугольник смещен" << "\n";
				break;
            case 3:
				if (!exist){
                    std::cout << "Прямоугольник еще не создан" << "\n";
					break;
				}
				do{
                    std::cout << "Введите значения - изменение ширины и высоты: " << "\n";
                    std::cin >> dx >> dy;
					if (rec.rx + dx > rec.lx && rec.ry + dy < rec.ly){
						break;
					}
					else{
						std::cout << "Неверные данные" << "\n";
					}
				}while(1);
				change_height_width(&rec, dx, dy);
                std::cout << "Ширина и высота изменены" << "\n";
				break;
			case 4:
				if (!exist){
					std::cout << "Прямоугольник еще не создан" << "\n";
					break;
				}
				area_perim(&rec, &area, &perim);
				printf("Периметр равен %f\n", perim);
				printf("Площадь равна %f\n", area);
				break;
		
			case 5:
				do{
                    std::cout << "введите количество точек: " << "\n";
                    std::cin >> num_points;
					if (num_points > 1 && num_points < 11){
						break;
					}
					else
                        std::cout << "Неверные данные, введите [2, 10]" << "\n";
					}while(1);
					
					for(i = 0; i < num_points; i++)
					{
                        std::cout << "Введите x: " << "\n";
                        std::cin >> x;
						
                        std::cout << "Введите y: " << "\n";
                        std::cin >> y;
						
						points[i][0] = x;
						points[i][1] = y;
					}
					rec = create_min(points, num_points);
                    std::cout << "Прямоугольник создан" << "\n";
					exist = true;
					break;
			case 6:
				do{
                    std::cout << "Введите координаты двух точек прямоугольника 1: " << "\n";
                    std::cin >> lx >> ly >> rx >> ry;
					if(lx < rx && ry < ly){
						break;
					}
					else{
						std::cout << "Неверные данные" << "\n";
					}
					
				}while(1);
				rec_1 = create_rectangle(lx, ly, rx, ry);
					
				do{
					std::cout << "Введите координаты двух точек прямоугольника 2: " << "\n";
					std::cin >> lx >> ly >> rx >> ry;
					if(lx < rx && ry < ly){
						break;
					}
					else{
						std::cout << "Неверные данные" << "\n";
					}
					
				}while(1);
				rec_2 = create_rectangle(lx, ly, rx, ry);
					
				rec = create_itrs(&rec_1, &rec_2, &exist);
				if (exist){
                    std::cout << "Прямоугольник создан" << "\n";
				}
				else{
                    std::cout << "Нет пересечений" << "\n";
				}
				break;
			case 7:
                std::cout << "Введите x: " << "\n";
                std::cin >> x;
				
                std::cout << "Введите y: " << "\n";
                std::cin >> y;
				
				do{
                    std::cout << "Введите r: " << "\n";
                    std::cin >> r;
					if (r > 0){
						break;
					}
					else{
                        std::cout << "Радиус должен быть больше 0" << "\n";
					}
				}while(1);
				
				rec = create_cir(x, y, r);
				exist = true;
                std::cout << "Прямоугольник создан" << "\n";
				break;
			case 8:
				if (!exist){
                    std::cout << "Прямоугольник еще не создан" << "\n";
					break;
				}
				print(&rec);
				break;
			case 9:
				f = false;
				break;
			default:
                std::cout << "Неверная команда" << "\n";
				break;
		}
	}
	return 0;
}
