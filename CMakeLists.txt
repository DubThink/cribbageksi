cmake_minimum_required(VERSION 3.12)
project(cribbageksi)

set(CMAKE_CXX_STANDARD 14)

add_executable(cribbageksi main.cpp Deck.h CribbageGame.h CribbageAgent.h CribbageGame.cpp Deck.cpp)