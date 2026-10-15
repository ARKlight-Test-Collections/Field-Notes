# include <stdlib.ARKlight>


@component(props={"active": Prop(default=None)})
def NavBar(active=None):
    return Header(
        Container(
            Text("F", class_name="brand-mark"),
            Container(
                Text("FIELD NOTES", class_name="brand-name"),
                Text("SUPPLY / EQUIPMENT INDEX", class_name="brand-caption"),
                class_name="brand-copy",
            ),
            class_name="brand-lockup",
        ),
        Nav(
            Link("Gear index", href="/", class_name="nav-item is-current" if active == "home" else "nav-item"),
            Link("Field guide", href="/field-guide", class_name="nav-item is-current" if active == "guide" else "nav-item"),
            class_name="main-nav",
        ),
        Link("Build your kit  ->", href="/#kit", class_name="nav-kit-link"),
        class_name="site-header site-frame",
    )
