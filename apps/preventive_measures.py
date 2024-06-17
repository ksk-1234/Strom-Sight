import streamlit as st

def app():
    # Set background color
    st.markdown(
        """
        <style>
        body {
            background-color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Overview of Cyclones
    st.markdown(
        """
        <div class="card">
            <div class="header">Overview of Cyclones</div>
            <div class="content">Cyclones are large-scale weather systems that rotate counterclockwise in the Northern Hemisphere and clockwise in the Southern Hemisphere. They typically form in tropical or subtropical regions and are fueled by warm ocean waters. Cyclones can vary in size and intensity, ranging from tropical depressions with sustained winds of less than 39 mph (63 km/h) to Category 5 hurricanes with winds exceeding 157 mph (252 km/h).</div>
            <img src="https://th.bing.com/th/id/OIG1.D2uqRy3mswVvjSmyAbZC?pid=ImgGn" alt="Cyclone Image" width="100%" />
        </div>
        """, unsafe_allow_html=True
    )
    
    # Preventive Measures
    st.markdown(
        """
        <div class="card">
            <div class="header">Preventive Measures</div>
        """, unsafe_allow_html=True
    )
    
    preventive_measures = [
        ("Stay Informed", 
        "Keep track of weather forecasts and advisories issued by local authorities. Stay tuned to radio, television, or official social media channels for updates.",
        "https://th.bing.com/th/id/OIG3.VHnKiGSRxSqvg0WvUMf_?pid=ImgGn"),
        ("Prepare an Emergency Kit", 
        "Assemble an emergency kit containing essential items such as non-perishable food, water, medications, flashlights, batteries, and important documents. Ensure that your emergency kit is easily accessible and kept in a designated location.",
        "https://th.bing.com/th/id/OIG2.9vbP7H0cT4bj3iqXrKEg?pid=ImgGn"),
        ("Secure Property", 
        "Secure your property by reinforcing windows and doors, trimming trees and bushes, and securing outdoor furniture to prevent damage from strong winds. Consider installing storm shutters or impact-resistant windows for added protection.",
        "https://th.bing.com/th/id/OIG4.TYikXXa25DNfpZ9fqMFT?pid=ImgGn"),
        ("Evacuate if Necessary", 
        "Follow evacuation orders issued by authorities. Have a designated evacuation route and plan in place, and evacuate to a safe location well in advance of the storm. Take your emergency kit with you and ensure that your pets are also safely evacuated.",
        "https://th.bing.com/th/id/OIG3.hjuHr1SwZiqhf.cgk1W0?w=1024&h=1024&rs=1&pid=ImgDetMain"),
        ("Stay Indoors During the Storm", 
        "Seek shelter indoors and stay away from windows, doors, and exterior walls. Avoid using candles and open flames, and use battery-powered devices for lighting and communication. Listen to local news updates and follow instructions from emergency officials.",
        "https://th.bing.com/th/id/OIG1.coT8FbAQHlJ0UqGroMRc?w=1024&h=1024&rs=1&pid=ImgDetMain"),
        ("After the Storm", 
        "Wait for authorities to declare it safe before returning home. Be cautious of downed power lines, flooding, and debris, and avoid walking or driving through floodwaters. Check your property for any damage and contact your insurance company if necessary.",
        "https://th.bing.com/th/id/OIG2.ZW3gy7bweKOerkraQS7e?pid=ImgGn")
    ]

    
    for measure, description, image_url in preventive_measures:
        st.markdown(
            f"""
            <div class="card">
                <div class="content">
                    <div class="text">
                        <h3>{measure}</h3>
                        <p>{description}</p>
                    </div>
                    <div class="image">
                        <img src="{image_url}" alt="{measure}" width="80%" />
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True
        )

    st.markdown("</div>", unsafe_allow_html=True)

    # CSS styling for header
    st.markdown(
        """
        <style>
        .card {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .header {
            color: #007bff;
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .content {
            display: flex;
            align-items: center;
        }
        .text {
            flex: 1;
            padding-right: 20px;
        }
        .text h3 {
            margin-bottom: 10px;
        }
        .text p {
            font-size: 16px;
            margin-bottom: 10px;
        }
        .image {
            flex: 1;
            text-align: right;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    app()
