# include <stdlib.ARKlight>

from components.footer import footer
from components.nav import NavBar
from content.site_content import CATEGORIES, DESCRIPTION, FAVICON, PRODUCTS, TITLE


def product_card(product):
    term_states = [
        f"term_{product['id']}_{index}"
        for index, _ in enumerate(product["search_terms"])
    ]
    return Show(
        Predicate.one_of("active_category", ["All gear", product["category"]]),
        Show(
            Predicate.or_("query_empty", *term_states),
            Article(
                Figure(
                    Image(src=product["image"], alt=product["alt"], class_name="product-image"),
                    FigCaption(product["code"], class_name="image-caption"),
                    class_name="product-figure",
                ),
                Container(
                    Container(
                        Text(product["badge"], class_name="product-badge"),
                        Text(product["category"].upper(), class_name="product-category"),
                        class_name="product-overline",
                    ),
                    Heading(product["name"], level=3, class_name="product-name"),
                    Text(product["description"], class_name="product-description"),
                    Details(
                        Summary("Field specifications"),
                        Text(product["spec"], class_name="spec-copy"),
                        class_name="product-details",
                    ),
                    Container(
                        Text(product["price"], class_name="product-price"),
                        Button(
                            "Add to kit +",
                            on_click=Action.append("kit", product["name"]),
                            class_name="add-button",
                        ),
                        class_name="product-action-row",
                    ),
                    class_name="product-copy",
                ),
                class_name="product-card",
            ),
        ),
    )


def home():
    term_states = [
        Computed(
            f"term_{product['id']}_{index}",
            deps=("query_upper",),
            derive=Derive.includes_substring("query_upper", term.upper()),
        )
        for product in PRODUCTS
        for index, term in enumerate(product["search_terms"])
    ]
    term_names = tuple(
        f"term_{product['id']}_{index}"
        for product in PRODUCTS
        for index, _ in enumerate(product["search_terms"])
    )

    def feature_intro():
        return Section(
            Container(
                Text("FIELD SYSTEMS / 04", class_name="eyebrow"),
                Heading("Field-ready gear.", level=1, class_name="page-title"),
                Text("Selected for the miles between trailheads.", class_name="intro-copy"),
                class_name="intro-copy-column",
            ),
            class_name="intro-band",
        )

    def catalog_tools():
        return Container(
            Container(
                Text("EXPLORE THE INDEX", class_name="eyebrow"),
                Text(Bind("active_category"), class_name="catalog-status"),
                class_name="catalog-heading",
            ),
            Container(
                Input(
                    type="search",
                    name="q",
                    placeholder="Search gear, use, or material",
                    aria_label="Search the gear index",
                    bind_value=Bind.model("query"),
                    class_name="search-input",
                ),
                Button("Clear", on_click=Action.set("query", ""), class_name="clear-button"),
                class_name="search-row",
            ),
            Container(
                *[
                    Button(
                        category,
                        on_click=Action.set("active_category", category),
                        class_name="category-button",
                    )
                    for category in CATEGORIES
                ],
                class_name="category-row",
            ),
            class_name="catalog-tools",
        )

    def catalog_section():
        return Section(
            catalog_tools(),
            Container(
                Container(
                    *[product_card(product) for product in PRODUCTS],
                    class_name="product-grid grid",
                ),
                Show(
                    Predicate.falsy("query_empty"),
                    Show(
                        Predicate.truthy("no_search_results"),
                        Container(
                            Text("NO MATCH IN THE INDEX", class_name="empty-title"),
                            Text("Try a product name, category, or field term such as shell, water, or shelter."),
                            Button("Reset search", on_click=Action.set("query", ""), class_name="clear-button"),
                            class_name="search-note",
                        ),
                    ),
                ),
                class_name="catalog-results",
            ),
            id="catalog",
            class_name="catalog-column",
        )

    def kit_panel():
        return Container(
            Text("PACK BUILDER / LIVE LIST", class_name="eyebrow kit-eyebrow"),
            Container(
                Heading("Your kit", level=2, class_name="kit-title"),
                Text(Bind("kit_count"), class_name="kit-count-large"),
                class_name="kit-heading",
            ),
            Text("A running list, saved on this device.", class_name="kit-description"),
            Progress(value=Bind("kit_count"), max="8", class_name="kit-progress"),
            Show(
                Predicate.is_empty("kit"),
                Container(
                    Text("Nothing packed yet.", class_name="empty-title"),
                    Text("Add an item from the index and it will appear here."),
                    class_name="kit-empty",
                ),
            ),
            Show(
                Predicate.is_not_empty("kit"),
                Container(
                    Repeat(
                        "kit",
                        template=lambda: Container(
                            Text(RepeatItem.value(), class_name="kit-item-name"),
                            Button(
                                "Remove",
                                on_click=Action.remove("kit", RepeatItem.index()),
                                class_name="remove-button",
                            ),
                            class_name="kit-row",
                        ),
                    ),
                    Container(
                        Text("ITEMS IN KIT", class_name="kit-total-label"),
                        Text(Bind("kit_count"), class_name="kit-total-number"),
                        class_name="kit-total",
                    ),
                    Button("Clear kit", on_click=Action.set("kit", []), class_name="clear-kit-button"),
                    class_name="kit-filled",
                ),
            ),
            class_name="kit-panel",
            id="kit",
        )

    def sidebar():
        return Container(
            kit_panel(),
            Container(
                Text("A FIELD NOTE", class_name="eyebrow"),
                Heading("Carry less. Choose well.", level=3, class_name="note-title"),
                Text("Every piece earns its place. Start with the conditions, then build around the essentials you trust.", class_name="field-note-copy"),
                Link("Read the field guide  ->", href="/field-guide", class_name="text-link"),
                class_name="field-note",
            ),
            class_name="sidebar-stack",
        )

    return Page(
        State("query", "", query="q"),
        State("active_category", "All gear"),
        State("kit", [], persist=True),
        State("zero", 0),
        Computed("query_upper", deps=("query",), derive=Derive.uppercase("query")),
        Computed("query_empty", deps=("query",), derive=Derive.is_empty("query")),
        Computed("kit_count", deps=("kit",), derive=Derive.count("kit")),
        *term_states,
        Computed("search_match_count", deps=term_names, derive=Derive.sum(*term_names)),
        Computed("no_search_results", deps=("search_match_count", "zero"), derive=Derive.compare("search_match_count", "zero", "eq")),
        NavBar(active="home"),
        Main(
            Container(
                feature_intro(),
                Container(catalog_section(), sidebar(), class_name="app-layout"),
                class_name="home-stack",
            ),
            class_name="site-frame app-content",
        ),
        footer(),
        title=TITLE,
        description=DESCRIPTION,
        favicon=FAVICON,
    )
