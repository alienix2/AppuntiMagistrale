# The project

## Main file

```go
func main() {
  gameManager := pg.NewGameSceneManager()
  gameManager.AddScene(gp.NewGameTitle())
  gameManager.AddScene(gp.InitGamePong())
}
```

## Scene manager

```go
type GameSceneManager struct {
  scenes []GameScenes
  currentScene uint
}

func (game *GameSceneManager) AddScene(scene GameScenes) {
  game.scenes = append(game.scenes, scene)
  scene.setManager(game)
}

func (game *GameSceneManager) GameLoop() {
  for !rl.WindowShouldClose() {
    //ToDo
  }
}
```

## Scene

```go
type GameScenes interface {
  RunScene()
  setManager(mgr *GameSceneManager)
}
```

## Game title

```go
type GameTitle struct {
  GamePong
}

func NewGameTitle() *GameTitle {
  game := InitGamePong()
  gmae.player = NewCpuPaddle() //To fill
  return &GameTitle{}
}

func (game *GameTitle) RunScene() {
  if rl.IsKeyDown(rl.KeyEnter) {
    //ToDo
  }
  else {
    //ToDo
  }
}
```

## Game pong

```go
type GamePong struct {
  player *PlayerPaddle
  cpu *CpuPaddle
  ball *Ball
  int playerScore
  int cpuScore
}
```

```go
type GameObject interface {
  Update()
  Draw()
  CheckCollision(obj GameObject)
  GetBoundingBox() Rectangle
}
```

We need to actually implement game objects for instance the ball:

```go
func (ball *Ball) Update() {
  //ToDo
}
```

Check Moodle for something more in-depth.
