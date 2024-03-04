#include <SFML/Graphics.hpp>
#include <SFML/System.hpp>
#include <vector>
#include <random>
#include "fish.h"
#include "hunter.h"
#include "plankton.h"

using namespace sf;

int main()
{
    srand(time(NULL));
    RenderWindow win(sf::VideoMode(1280, 720), L"Аквариум");
    Image icon;
    if (!icon.loadFromFile("Image/pole.jpg")) {
        return 1;
    }
    win.setIcon(32, 32, icon.getPixelsPtr());

    //поле
    Texture texturPole;
    texturPole.loadFromFile("Image/pole.jpg");
    RectangleShape GamePole(Vector2f(1280,720));
    GamePole.setTexture(&texturPole);
    GamePole.setPosition(Vector2f(0, 0));

    Vector2f pos;

    // Создание списка рыбок, питающихся планктоном
    std::vector<fish> herbivorous_fishes;
    for (int i = 0; i < 10; i++) {
        herbivorous_fishes.push_back(fish());
    }

    std::vector<hunter> herbivorous_hunters;
    for (int i = 0; i < 10; i++) {
        herbivorous_hunters.push_back(hunter());
    }

    std::vector<plankton> herbivorous_planktons;
    for (int i = 0; i < 10; i++) {
        herbivorous_planktons.push_back(plankton());
    }

    // Часы для отслеживания времени
    sf::Clock clock;

    while (win.isOpen())
    {
        sf::Event event;
        
        clock.restart();
        while (win.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                win.close();
        }
        float dt = clock.restart().asSeconds();
        for (auto& herbivorous_fish : herbivorous_fishes) {
            herbivorous_fish.update(dt);
        }
        for (auto& herbivorous_hunter : herbivorous_hunters) {
            herbivorous_hunter.update(dt);
        }
        for (auto& herbivorous_plankton : herbivorous_planktons) {
            herbivorous_plankton.update(dt);
        }
        win.clear();
        win.draw(GamePole);
        for (auto& herbivorous_fish : herbivorous_fishes) {
            herbivorous_fish.draw(win);
        }
        for (auto& herbivorous_hunter : herbivorous_hunters) {
            herbivorous_hunter.draw(win);
        }
        for (auto& herbivorous_plankton : herbivorous_planktons) {
            herbivorous_plankton.draw(win);
        }
        win.display();
    }
    return 0;
}