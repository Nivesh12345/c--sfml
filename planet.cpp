#include <SFML/Graphics.hpp>
#include <iostream>
using namespace std;
#include <cmath>


    
    
class planet
{
    
    sf::CircleShape s;
    sf::CircleShape s1;
    sf::Vertex line[2];

    int radius;
    int distance;
    float speed;
    float angle = 0;
    int width = 1000;
    int height = 1000;
    float x = width / 2;
    float y = height / 2;
    double ex = 0;
    double ey = 0;
    int r, g, b;
public:
    planet(float radius, float distance,float speed,int r, int g, int b)
    {
        

        this->radius = radius;
        this->distance = distance;
        this->speed = speed;
        this->r = r;
        this->g = g;
        this->b = b;
        //s.setPosition(pos);
        s.setFillColor(sf::Color(r,g,b));
        s.setRadius(radius);
        
        s1.setRadius(distance);
        s1.setFillColor(sf::Color::Transparent);
        s1.setOutlineColor(sf::Color(r,g,b));
        s1.setOutlineThickness(2);
        s1.setPosition(x - distance, y - distance);
    }

    void render(sf::RenderWindow& wind)
    {
        wind.draw(s1);
        wind.draw(line, 5, sf::Lines);
        wind.draw(s);
    }

    void move()
    {   
        ex = ((cos(angle) * distance) + x) - radius;
        ey = ((sin(angle) * distance) + y) - radius;
        angle += speed;
        s.setPosition(ex,ey);
        
        line[0].position = sf::Vector2f(x, y);
        line[0].color = sf::Color(r, g, b);
        line[1].position = sf::Vector2f(ex+radius, ey+radius);
        line[1].color = sf::Color(r, g, b);
        



    }

};





int main()
{
    int radius =30;
    int radius1 = 20;
    int width = 1000;
    int height = 1000;
    float x = width / 2;
    float y = height / 2;
    double rd = (radius / sqrt(2));
    float angle = 0;
    
    

    sf::RenderWindow window(sf::VideoMode(width, height), "My Program");
    window.setFramerateLimit(60);
    //------------------------sun----------------------------
    sf::CircleShape circle;
    circle.setRadius(radius);
    circle.setFillColor(sf::Color::Yellow);
    
    

    //-------------------------planet------------------------

    planet p(20,200,0.04, 0, 255, 0);
    planet p1(20, 270, 0.03, 255, 140, 0);
    planet p2(20, 330, 0.02, 0, 191, 255);
    planet p3(20, 400, 0.01, 138, 43, 226);

    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();
        }



        
        circle.setPosition(x - radius, y - radius);
       
        //--------------------moving the planet------------------------------
        p.move();
        p1.move();
        p2.move();
        p3.move();
        //-----------------------------------x-x-x-x-x-x---------------------------
        window.clear();
        p.render(window);
        p1.render(window);
        p2.render(window);
        p3.render(window);


        window.draw(circle);
        
        
        window.display();
    }



    return 0;
}
