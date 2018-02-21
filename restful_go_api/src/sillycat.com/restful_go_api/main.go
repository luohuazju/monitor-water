package main

import "github.com/gin-gonic/gin"
import "sillycat.com/restful_go_api/waterrecord"

var DB = make(map[string]string)

func setupRouter() *gin.Engine {
	// Disable Console Color
	// gin.DisableConsoleColor()
	router := gin.Default()

	// Ping test
	router.GET("/ping", func(c *gin.Context) {
		c.String(200, "pong")
	})

	v1 := router.Group("api/v1")
	{
		v1.GET("/instructions", waterrecord.GetInstructions)
		v1.GET("/instructions/:id", waterrecord.GetInstruction)
		v1.POST("/instructions", waterrecord.PostInstruction)
		v1.PUT("/instructions/:id", waterrecord.UpdateInstruction)
		v1.DELETE("/instructions/:id", waterrecord.DeleteInstruction)
	}

	return router
}

func main() {
	router := setupRouter()
	// Listen and Server in 0.0.0.0:8080
	router.Run(":8080")
}
