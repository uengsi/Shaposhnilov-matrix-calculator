#pragma once
#include <SFML/Graphics.hpp>
#include <random>
using namespace sf;

class hunter {
public:
    hunter();
    void update(float dt);
    void draw(sf::RenderWindow& window);
private:
    sf::Vector2f pos;
    sf::Vector2f speed;
    float lifetime;
    float reproduction_rate;
    float sight_range;
};
