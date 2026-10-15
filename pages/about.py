# include <stdlib.ARKlight>

from components.footer import footer
from components.nav import NavBar
from content.site_content import DESCRIPTION, FAVICON, TITLE


def field_guide():
    return Page(
        NavBar(active="guide"),
        Main(
            Section(
                Text("FIELD GUIDE / 01", class_name="eyebrow"),
                Heading("A better kit starts with the conditions.", level=1, class_name="guide-title"),
                Text("A short checklist for choosing what earns a place in your pack.", class_name="guide-intro"),
                Image(
                    src="https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1800&q=90",
                    alt="Mountain range at the edge of a remote hiking route",
                    class_name="guide-image",
                ),
                class_name="guide-opening",
            ),
            Container(
                Article(
                    Text("01 / START WITH WEATHER", class_name="eyebrow"),
                    Heading("Plan for the turn, not the forecast.", level=2, class_name="guide-section-title"),
                    Text("Forecasts are useful at the trailhead. Exposure, elevation, and time outside decide what you actually need. Keep a shell and a warm layer accessible, even when the morning looks settled."),
                    class_name="guide-entry",
                ),
                Article(
                    Text("02 / PROTECT THE NIGHT", class_name="eyebrow"),
                    Heading("Shelter and sleep are the foundation.", level=2, class_name="guide-section-title"),
                    Text("Choose a shelter for the worst likely conditions, then test the whole sleep system before the trip. A small comfort gained overnight makes the next day's decisions better."),
                    class_name="guide-entry",
                ),
                Article(
                    Text("03 / KEEP THE SYSTEM SIMPLE", class_name="eyebrow"),
                    Heading("Every item should do a clear job.", level=2, class_name="guide-section-title"),
                    Text("A dependable water plan, light, and way to prepare food cover the basics. Add specialized equipment only when the route or conditions make the reason obvious."),
                    class_name="guide-entry",
                ),
                class_name="guide-grid",
            ),
            Details(
                Summary("A quick pre-departure check"),
                List(
                    Item("Check the route, water sources, and turnaround time."),
                    Item("Match layers and shelter to exposure, not just temperature."),
                    Item("Test lighting, filtration, and stove before leaving."),
                    Item("Leave a route plan with someone at home."),
                ),
                class_name="guide-checklist",
            ),
            Link("Return to the gear index  ->", href="/", class_name="text-link guide-return"),
            class_name="site-frame guide-content",
        ),
        footer(),
        title=f"Field guide | {TITLE}",
        description=DESCRIPTION,
        favicon=FAVICON,
    )
