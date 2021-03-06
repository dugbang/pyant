### 개미 군집 시뮬레이션 기능 구현

* 유튜브에서 본 것을 직접 구현해보고 싶어졌다.
* 공부해야 할 것이 생각보다 많다. 오래 걸릴 것 같다.

### 작업하기

1. ~~pygame 에서 물체의 랜덤 워크를 구현해보자.~~
1. ~~좌표계와 맵의 관계를 정의하자.~~
1. ~~임의의 영역으로 이동하기~~
1. 집과 타겟(음식) 영역 설정하기
1. 이동가능한 영역 계산하기
1. 회귀 로직 작성하기
1. 지우게(경로 삭제) 기능을 구현해보자

### 작업일지

#### 20210423

* 복수개의 객체를 임의의 위치로 이동하기
* 전체적인 코드 정리
  - sprite.Group 을 list 로 변경
    
#### 20210422

* 임의의 위치로 이동하기
* 인접한 영역 중에 임의의 영역을 선택하는 기능 구현

#### 20210421

* 새영역에 진입할 때 marker 표시하기
* pygame.sprite.Sprite 에서 Ant 정의

#### 20210420

* 랜덤 워크 이동 영역 제한
* marker 사라지는 효과 구현 (fade off)

#### 20210420

* 좌표계와 맵의 기본 틀 작성
* marker 기능 구현

#### 20210419

* 랜덤 워크 기능 구현
   - 이동 속도는 고정한다.
   - 방향을 랜덤하게 변경한다. 

### 참고 사이트

1. [C++ Ants Simulation](https://youtu.be/81GQNPJip2Y)
    - [AntSimulator](https://github.com/johnBuffer/AntSimulator)
1. [Build an Asteroids Game With Python and Pygame](https://realpython.com/asteroids-game-python/)
1. [PyGame: A Primer on Game Programming in Python](https://realpython.com/pygame-a-primer/)
