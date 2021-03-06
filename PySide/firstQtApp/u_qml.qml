import QtQuick.Window 2.2 as UQml
import "qmls" as Uqmls
import "jscripts/u_js.js" as Ujs

UQml.Window {
    visible: true
    width: 350
    height: 590    
    title: qsTr("First Qml")
    UQml.Rectangle {        
        color: "#FF0000"        
        width: 140        
        height: 140        
        border.color: "#FF0000"        
        border.width: 1
        radius: width * 0.5
    }
    Uqmls.UCircle {
        id: rcircle        
        anchors.centerIn: parent
        }    
        MouseArea {        
            anchors.fill: parent        
            onClicked: rcircle.height = Ujs.hsize(rcircle.height);    
        }
    }
    Uqmls.URect {        
        id: rect1
        color: "#000000"
        width: parent.width - (parent.width / 5)        
        height: parent.height        
        MouseArea {            
            anchors.fill: parent            
            onClicked: rect1.color = "#222222";        
        }
        Uqmls.UText {
            id: utext1            
            x: 20            
            y: 50            
            font.family: "Open"            
            font.pixelSize: 37            
            width: rect1.width - (20 * 2)            
            text: "text 1"       
        }        
        Uqmls.UText {            
            id: utext2            
            x: 20            
            y: utext1.height + (50 * 2)            
            font.family: "Verdana"            
            font.pixelSize: 27            
            width: rect1.width - (20 * 2)        
        }        
        Uqmls.UText {            
            id: utext3            
            x: 20            
            y: (utext1.height + utext2.height) + (50 * 3)            
            font.family: "Open Sans"            
            font.pointSize: 14            
            width: rect1.width - (20 * 2)        
        }
    }
    Uqmls.URect {        
        id: rect2        
        color: "#00293b"        
        x: rect1.width        
        width: parent.width / 5        
        height: parent.height        
        MouseArea {            
            anchors.fill: parent            
            onClicked: rect2.color = "#340147";   
            utext2.text = "text 2";                
            utext3.text = "text 3";     
        }    
    }
}
