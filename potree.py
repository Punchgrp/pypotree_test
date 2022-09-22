import laspy
import pandas as pd
import streamlit as st
from streamlit_folium import folium_static
import streamlit.components.v1 as components
import pypotree

st.title('Streamlit Potree Example 2')

lasdata1 = "/content/Ayutthaya_line_4.laz"

print("Load Data...")
new = laspy.read(lasdata1)
new2 = laspy.read(lasdata1)
#xyz_load = np.asarray(new.points)

print("To Pandas...")
#df = pd.DataFrame({'x':list(new.x),'y':list(new.y),'z':list(new.z),'red':list(new.red),'green':list(new.green),'blue':list(new.blue)})
df = pd.DataFrame({'x':list(new.x),'y':list(new.y),'z':list(new.z)})
print("Pandas Finish...")

df2 = df.sample(100000)
df3 = df2.to_numpy()
st.write("Load Point Cloud...")
components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <div id="accordion">
      <div class="card">
        <div class="card-header" id="headingOne">
          <h5 class="mb-0">
            <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
            Collapsible Group Item #1
            </button>
          </h5>
        </div>
        <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
          <div class="card-body">
            Collapsible Group Item #1 content
          </div>
        </div>
      </div>
      <div class="card">
        <div class="card-header" id="headingTwo">
          <h5 class="mb-0">
            <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
            Collapsible Group Item #2
            </button>
          </h5>
        </div>
        <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
          <div class="card-body">
            Collapsible Group Item #2 content
          </div>
        </div>
      </div>
    </div>
    """, 
    width=1200,
    height=800,
)
cloudpath = pypotree.generate_cloud_for_display(df3)
show = pypotree.display_cloud_colab(cloudpath)
B4 = "https://s3.ap-southeast-1.amazonaws.com/triconeer.com/centrovision/potreedemo/B4.html"
components.iframe(B4, width=900, height=1000, scrolling=True)
st.write(show)
components.html(
  """
	document.title = "";
	viewer.setEDLEnabled(true);
	viewer.setBackground("gradient"); // ["skybox", "gradient", "black", "white"];
	viewer.setDescription(`PyPotree_Test`);

<div class="potree_container" style="position: absolute; width: 100%; height: 500px; left: 0px; top: 0px; ">
	<div id="potree_render_area"></div>
	<div id="potree_sidebar_container"> </div>
</div>

<script>

	window.viewer = new Potree.Viewer(document.getElementById("potree_render_area"));

	viewer.setEDLEnabled(true);
	viewer.setFOV(60);
	viewer.setPointBudget(1*1000*1000);
	document.title = "";
	viewer.setEDLEnabled(true);
	viewer.setBackground("gradient"); // ["skybox", "gradient", "black", "white"];
	viewer.setDescription(``);
	viewer.loadSettingsFromURL();

	viewer.loadGUI(() => {
		viewer.setLanguage('en');
		// $("#menu_appearance").next().show();
		// $("#menu_tools").next().show();
		// $("#menu_scene").next().show();
		// viewer.toggleSidebar();
	});

	Potree.loadPointCloud("https://localhost:15595/point_clouds/pointclouds/4b3771/cloud.js", "4b3771", e => {
		let pointcloud = e.pointcloud;
		let material = pointcloud.material;
		viewer.scene.addPointCloud(pointcloud);
		material.pointColorType = Potree.PointColorType.ELEVATION; // any Potree.PointColorType.XXXX 
		material.size = 1;
		material.pointSizeType = Potree.PointSizeType.ADAPTIVE;
		material.shape = Potree.PointShape.SQUARE;
		viewer.fitToScreen();
	});

</script>
"""  , width=1200, height=800, scrolling=False)
