#include "hunter.h"
#include <random>

hunter::hunter() {
    // Случайное положение
    pos = sf::Vector2f(rand() % 800, rand() % 600);
    // Случайная скорость
    speed = sf::Vector2f(5000, 5000);
    // Случайное время жизни
    lifetime = rand() % 1000 + 1000;
    // Случайная частота размножения
    reproduction_rate = rand() % 100 + 100;
    // Случайная дальность зрения
    sight_range = rand() % 100 + 100;
}

void hunter::update(float dt) {
    // Обновление положения
    pos += speed * dt;
    // Ограничение положения
    if (pos.x < 0) {
        pos.x = 0;
        speed.x = -speed.x;
    }
    if (pos.y < 0) {
        pos.y = 0;
        speed.y = -speed.y;
    }
    if (pos.x > 720) {
        pos.x = 720;
        speed.x = -speed.x;
    }
    if (pos.y > 1280) {
        pos.y = 1280;
        speed.y = -speed.y;
    }
}

void hunter::draw(sf::RenderWindow& window) {
    Texture texturfish;
    texturfish.loadFromFile("Image/hunter.png");
    RectangleShape Gamefish(Vector2f(100, 50));
    Gamefish.setTexture(&texturfish);
    Gamefish.setPosition(pos);
    window.draw(Gamefish);
}