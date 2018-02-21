package waterrecord

import (
	"github.com/gin-gonic/gin"
	//"strconv"
)

func GetInstructions(c *gin.Context) {
	c.JSON(200, gin.H{"ok": "GET api/v1/waterrecords"})
}

func GetInstruction(c *gin.Context) {
	c.JSON(200, gin.H{"ok": "GET api/v1/waterrecords/1"})
}

func PostInstruction(c *gin.Context) {
	c.JSON(200, gin.H{"ok": "POST api/v1/waterrecords"})

}

func UpdateInstruction(c *gin.Context) {
	c.JSON(200, gin.H{"ok": "PUT api/v1/waterrecords/1"})

}

func DeleteInstruction(c *gin.Context) {
	c.JSON(200, gin.H{"ok": "DELETE api/v1/waterrecords/1"})
}
