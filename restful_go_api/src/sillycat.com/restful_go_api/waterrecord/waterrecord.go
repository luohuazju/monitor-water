package waterrecord

import (
	"github.com/gin-gonic/gin"
	"log"
	"sillycat.com/restful_go_api/common"
	"strconv"
	"time"
)

type WaterRecord struct {
	Id          int64
	Location    string    `xorm:"location varchar(256) not null"`
	StartTime   string    `xorm:"start_time varchar(256) not null"`
	EndTime     string    `xorm:"end_time varchar(256) not null"`
	Duration    int       `xorm:"duration int(11)"`
	ReleaseDate string    `xorm:"release_date varchar(256)"`
	CreateDate  time.Time `xorm:"create_date DATETIME "`
	UpdateDate  time.Time `xorm:"update_date DATETIME"`
}

var engine = common.GetDatabase()

func (waterRecord WaterRecord) TableName() string {
	return "water_monitor"
}

func GetWaterRecords(c *gin.Context) {
	var items []WaterRecord
	query := "SELECT id, location, start_time, end_time, duration, release_date, create_date, update_date FROM water_monitor"
	err := engine.Sql(query).Find(&items)
	if err != nil {
		log.Fatal("Get err when exec query: ", err)
	}
	log.Println("query result: ", items)
	c.JSON(200, items)
}

func GetWaterRecord(c *gin.Context) {
	var item WaterRecord
	id := c.Param("id")

	has, err := engine.Where("id = ?", id).Get(&item)
	if err != nil {
		log.Fatal("Get one item err: ", err)
	}
	if has {
		c.JSON(200, item)
	} else {
		c.JSON(404, gin.H{"error": "WaterRecord not found"})
	}
}

func PostWaterRecord(c *gin.Context) {
	var item WaterRecord
	c.Bind(&item)

	if item.Location != "" && item.ReleaseDate != "" {
		_, err := engine.Insert(&item)
		if err != nil {
			log.Fatal("Insert fail:", err)
		} else {
			c.JSON(201, item)
		}
	} else {
		c.JSON(422, gin.H{"error": "fields are empty!"})
	}

}

func UpdateWaterRecord(c *gin.Context) {
	var item WaterRecord
	id := c.Param("id")
	c.Bind(&item)

	has, err := engine.SQL("select * from water_monitor where id = ?", id).Exist()
	if err != nil {
		log.Fatal("Fail to find item:", err)
	} else {
		if has {
			item.Id, _ = strconv.ParseInt(id, 0, 64)
			_, err := engine.Id(id).Update(&item)
			if err != nil {
				log.Fatal("Fail to update item:", err)
			} else {
				c.JSON(200, item)
			}
		} else {
			c.JSON(404, gin.H{"error": "Water Record not found"})
		}
	}
}

func DeleteWaterRecord(c *gin.Context) {
	id := c.Param("id")

	item := new(WaterRecord)

	has, err := engine.SQL("select * from water_monitor where id = ?", id).Exist()
	if err != nil {
		log.Fatal("Fail to find item:", err)
	} else {
		if has {
			//itemID, _ := strconv.ParseInt(id, 0, 64)
			_, err := engine.Where("id = ?", id).Delete(item)
			if err != nil {
				log.Fatal("Fail to delete:", err)
			} else {
				c.JSON(202, gin.H{"id": id})
			}
		} else {
			c.JSON(404, gin.H{"error": "Water Record not found"})
		}
	}
}
