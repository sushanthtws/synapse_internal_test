import streamlit as st
import requests

API_URL = "http://127.0.0.1:8001"

st.set_page_config(page_title="Skill Repository", layout="wide")

st.title("🚀 AI Skill Repository")


# -----------------------------
# STATE
# -----------------------------
if "selected_skill" not in st.session_state:
    st.session_state.selected_skill = None


# -----------------------------
# LOAD SKILLS
# -----------------------------
def load_skills():
    try:
        return requests.get(f"{API_URL}/skills").json()
    except:
        st.error("Backend not running on 8001")
        return []


skills = load_skills()


# -----------------------------
# SIDEBAR FILTERS
# -----------------------------
st.sidebar.header("🔎 Filters")

search = st.sidebar.text_input("Search skills")

all_tags = []
for s in skills:
    all_tags.extend(s.get("tags", []))

unique_tags = sorted(list(set(all_tags)))

tag_filter = st.sidebar.selectbox("Tag", ["all"] + unique_tags)


def filter_skills(skills, search, tag):
    out = skills

    if search:
        out = [
            s for s in out
            if search.lower() in s["title"].lower()
            or search.lower() in s["description"].lower()
        ]

    if tag != "all":
        out = [s for s in out if tag in s.get("tags", [])]

    return out


skills = filter_skills(skills, search, tag_filter)


# -----------------------------
# UPLOAD
# -----------------------------
st.markdown("## 📤 Upload Skill Markdown")

file = st.file_uploader("Upload .md file", type=["md"])

if file and st.button("Upload"):
    res = requests.post(
        f"{API_URL}/upload-md",
        files={"file": (file.name, file.getvalue(), "text/markdown")}
    )

    if res.status_code == 200:
        st.success("Uploaded successfully!")
        st.rerun()
    else:
        st.error("Upload failed")


st.markdown("---")


# -----------------------------
# DETAIL VIEW
# -----------------------------
if st.session_state.selected_skill:
    skill = st.session_state.selected_skill

    if st.button("⬅ Back"):
        st.session_state.selected_skill = None
        st.rerun()

    st.markdown(f"""
# 🔐 {skill['title']} ✓ Verified  
**Platform:** Platform Security Guild · v1.0  

---

### 📄 Description
{skill['description']}

### 🏷️ Tags
{" ".join(skill.get('tags', []))}
""")

    st.stop()


# -----------------------------
# GRID VIEW (GITHUB STYLE)
# -----------------------------
st.markdown("## 📦 Skills")

cols = st.columns(2)

if not skills:
    st.info("No skills found. Upload a markdown file.")

for i, s in enumerate(skills):
    with cols[i % 2]:

        st.markdown(f"""
### 🔐 {s['title']} ✓ Verified  
**Platform:** Platform Security Guild · v1.0  

> {s['description']}
""")

        if s.get("tags"):
            st.write("🏷️ " + ", ".join(s["tags"]))

        c1, c2, c3 = st.columns(3)

        with c1:
            if st.button("Open", key=f"open_{s['id']}"):
                st.session_state.selected_skill = s
                st.rerun()

        with c2:
            if st.button("👍", key=f"up_{s['id']}"):
                requests.post(f"{API_URL}/skills/{s['id']}/vote?value=1")

        with c3:
            if st.button("👎", key=f"down_{s['id']}"):
                requests.post(f"{API_URL}/skills/{s['id']}/vote?value=-1")

        st.markdown("---")