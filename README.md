# Microservice A

# Description
This microservice converts between color names and their corresponding hex codes. The service handles two types of requests:
1. **Hex Code**: Sends a color name corresponding to the provided hex code.
2. **Color Name**: Sends the hex code corresponding to the provided color name.
The microservice communicates via Python sockets.

# How to Programmatically Request Data
To request data from the microservice, create a socket connection and send either a hex code or a color name to the microservice. 

**Example for Sending Hex Code:**

```python
import socket

# set up socket connection to the microservice
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('localhost', 12345))

    # send the hex code
    s.sendall('#010101'.encode())

    # receive the response from the microservice
    response = s.recv(1024).decode()

print(f"Response: {response}")
```

**Example for Sending Color Name:**

```python
import socket

# set up socket connection to the microservice
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('localhost', 12345)

    # send color name
    s.sendall('white'.encode())

    # receive response from the microservice
    response = s.recv(1024).decode()

print(f"Response: {response}")
```

**UML Sequence Diagram**

<mxfile host="app.diagrams.net" agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36" version="27.0.6">
  <diagram name="Page-1" id="DL1c7x-kJyK4ogNbDzSz">
    <mxGraphModel dx="1452" dy="991" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="zu34gTwgS4UaY_RAdP6U-2" value="" style="endArrow=none;dashed=1;html=1;rounded=0;fontSize=12;startSize=8;endSize=8;curved=1;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="601" y="560" as="sourcePoint" />
            <mxPoint x="601" y="280" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="zu34gTwgS4UaY_RAdP6U-3" value="" style="endArrow=none;dashed=1;html=1;rounded=0;fontSize=12;startSize=8;endSize=8;curved=1;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="120" y="560" as="sourcePoint" />
            <mxPoint x="120" y="280" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="zu34gTwgS4UaY_RAdP6U-4" value="UML Sequence Diagram" style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;fontSize=16;" vertex="1" parent="1">
          <mxGeometry x="260" y="200" width="200" height="30" as="geometry" />
        </mxCell>
        <mxCell id="zu34gTwgS4UaY_RAdP6U-5" value="Client" style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;fontSize=16;" vertex="1" parent="1">
          <mxGeometry x="90" y="240" width="60" height="30" as="geometry" />
        </mxCell>
        <mxCell id="zu34gTwgS4UaY_RAdP6U-6" value="Microservice" style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;fontSize=16;" vertex="1" parent="1">
          <mxGeometry x="550" y="240" width="110" height="30" as="geometry" />
        </mxCell>
        <mxCell id="zu34gTwgS4UaY_RAdP6U-7" value="send string with hex code or color name" style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;fontSize=16;" vertex="1" parent="1">
          <mxGeometry x="210" y="300" width="310" height="30" as="geometry" />
        </mxCell>
        <mxCell id="zu34gTwgS4UaY_RAdP6U-9" value="receive request" style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;fontSize=16;" vertex="1" parent="1">
          <mxGeometry x="290" y="360" width="130" height="30" as="geometry" />
        </mxCell>
        <mxCell id="zu34gTwgS4UaY_RAdP6U-10" value="send response with color name or hex code" style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;fontSize=16;" vertex="1" parent="1">
          <mxGeometry x="190" y="430" width="330" height="30" as="geometry" />
        </mxCell>
        <mxCell id="zu34gTwgS4UaY_RAdP6U-11" value="receive response" style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;fontSize=16;" vertex="1" parent="1">
          <mxGeometry x="280" y="500" width="150" height="30" as="geometry" />
        </mxCell>
        <mxCell id="zu34gTwgS4UaY_RAdP6U-15" value="" style="endArrow=none;dashed=1;html=1;rounded=0;fontSize=12;startSize=8;endSize=8;curved=1;" edge="1" parent="1" target="zu34gTwgS4UaY_RAdP6U-7">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="130" y="314.67" as="sourcePoint" />
            <mxPoint x="200" y="315" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="zu34gTwgS4UaY_RAdP6U-16" value="" style="endArrow=classic;html=1;rounded=0;fontSize=12;startSize=8;endSize=8;curved=1;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="520" y="444.55" as="sourcePoint" />
            <mxPoint x="590" y="444.55" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="zu34gTwgS4UaY_RAdP6U-17" value="" style="endArrow=none;dashed=1;html=1;rounded=0;fontSize=12;startSize=8;endSize=8;curved=1;" edge="1" parent="1" source="zu34gTwgS4UaY_RAdP6U-11">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="450" y="520" as="sourcePoint" />
            <mxPoint x="580" y="515" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="zu34gTwgS4UaY_RAdP6U-18" value="" style="endArrow=none;dashed=1;html=1;rounded=0;fontSize=12;startSize=8;endSize=8;curved=1;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="430" y="374.52" as="sourcePoint" />
            <mxPoint x="590" y="375" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="zu34gTwgS4UaY_RAdP6U-19" value="" style="endArrow=classic;html=1;rounded=0;fontSize=12;startSize=8;endSize=8;curved=1;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="290" y="374.64" as="sourcePoint" />
            <mxPoint x="130" y="375" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="zu34gTwgS4UaY_RAdP6U-21" value="" style="endArrow=none;dashed=1;html=1;rounded=0;fontSize=12;startSize=8;endSize=8;curved=1;entryX=0.01;entryY=0.505;entryDx=0;entryDy=0;entryPerimeter=0;" edge="1" parent="1" target="zu34gTwgS4UaY_RAdP6U-10">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="130" y="445" as="sourcePoint" />
            <mxPoint x="190" y="444.55" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="zu34gTwgS4UaY_RAdP6U-22" value="" style="endArrow=classic;html=1;rounded=0;fontSize=12;startSize=8;endSize=8;curved=1;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="290" y="514.44" as="sourcePoint" />
            <mxPoint x="130" y="514.44" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="zu34gTwgS4UaY_RAdP6U-23" value="" style="endArrow=classic;html=1;rounded=0;fontSize=12;startSize=8;endSize=8;curved=1;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="520" y="320" as="sourcePoint" />
            <mxPoint x="590" y="320" as="targetPoint" />
          </mxGeometry>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
