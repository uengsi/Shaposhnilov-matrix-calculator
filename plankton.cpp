#include "plankton.h"
#include <random>

plankton::plankton() {
    // ��������� ���������
    pos = sf::Vector2f(rand() % 800, rand() % 600);
    // ��������� ��������
    speed = sf::Vector2f(5000, 5000);
    // ��������� ����� �����
    lifetime = rand() % 1000 + 1000;
    // ��������� ������� �����������
    reproduction_rate = rand() % 100 + 100;
    // ��������� ��������� ������
    sight_range = rand() % 100 + 100;
}

void plankton::update(float dt) {
    // ���������� ���������
    pos += speed * dt;
    // ����������� ���������
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

void plankton::draw(sf::RenderWindow& window) {
    Texture texturfish;
    texturfish.loadFromFile("Image/plankton.png");
    RectangleShape Gamefish(Vector2f(50, 25));
    Gamefish.setTexture(&texturfish);
    Gamefish.setPosition(pos);
    window.draw(Gamefish);
}