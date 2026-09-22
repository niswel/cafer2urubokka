# -*- coding: utf-8 -*-
"""Generates the menu tabs/panels HTML and carousel HTML from structured data,
so the large bilingual menu doesn't have to be hand-typed into index.html."""

import json

MENU = [
    ("fruit-salad", "Fruit Salad", "ෆෘට් සැලඩ්", [
        ("Fruit Salad with Vanilla Ice Cream", "ෆෘට් සැලඩ් සමග වැනිලා අයිස්ක්‍රීම්", 380),
        ("Fruit Salad with Chocolate Ice Cream", "ෆෘට් සැලඩ් සමග චොකලට් අයිස්ක්‍රීම්", 380),
        ("Fruit Salad with Strawberry Ice Cream", "ෆෘට් සැලඩ් සමග ස්ට්‍රෝබෙරි අයිස්ක්‍රීම්", 380),
        ("Fruit Salad with Fruit & Nut Ice Cream", "ෆෘට් සැලඩ් සමග ෆෘට් ඇන්ඩ් නට් අයිස්ක්‍රීම්", 420),
        ("Fruit Salad with Mix Ice Cream", "ෆෘට් සැලඩ් සමග මිශ්‍ර අයිස්ක්‍රීම්", 400),
        ("Fruit Yoghurt and Peanuts", "පලතුරු යෝගට් සමග රටකජු", 320),
        ("Only Fruit Salad", "පළතුරු පමණක්", 280),
    ]),
    ("hot-beverage", "Hot Beverage", "උණු පාන", [
        ("Plain Tea", "ප්ලේන් ටී", 60),
        ("Milk Tea", "කිරි තේ", 80),
        ("Black Coffee", "කෝපි", 100),
        ("Milk Coffee", "කිරි කෝපි", 120),
        ("Ginger Tea", "ඉඟුරු තේ", 90),
        ("Cardamom Tea", "එනසල් තේ", 90),
        ("Chai Tea", "චායි තේ", 110),
        ("Green Tea", "ග්‍රීන් තේ", 100),
        ("Hot Milo", "හොට් මයිලෝ", 130),
        ("Hot Chocolate", "හොට් චොකලට්", 150),
    ]),
    ("lassi", "Lassi", "ලැසී", [
        ("Mango Lassi", "අඹ ලැසී", 280),
        ("Banana Lassi", "කෙසෙල් ලැසී", 260),
        ("Avocado Lassi", "අලිගැටපේර ලැසී", 280),
        ("Mix Fruit Lassi", "මිශ්‍ර පළතුරු ලැසී", 300),
        ("Wood Apple Lassi", "දිවුල් ලැසී", 280),
    ]),
    ("smoothie", "Smoothie", "ස්මූති", [
        ("Avocado Smoothie", "අලිගැටපේර ස්මූති", 300),
        ("Mango Smoothie", "අඹ ස්මූති", 300),
        ("Banana Smoothie", "කෙසෙල් ස්මූති", 280),
        ("Papaya Smoothie", "ගස්ලබු ස්මූති", 280),
    ]),
    ("mojito", "Mojito", "මොජිටෝ", [
        ("Blue Lagoon Mojito", "බ්ලූ ලැගුන් මොජිටෝ", 350),
        ("Watermelon Mojito", "කොමඩු මොජිටෝ", 320),
        ("Orange Mojito", "ඔරේන්ජ් මොජිටෝ", 320),
        ("Lime Mojito", "දෙහි මොජිටෝ", 300),
        ("Blackcurrant Mojito", "බ්ලැක්කරන්ට් මොජිටෝ", 340),
        ("Passion Mojito", "පැෂන් මොජිටෝ", 320),
    ]),
    ("milkshake", "Milk Shake", "මිල්ක් ෂේක්", [
        ("Faluda Milk Shake", "ෆලුඩා මිල්ක් ෂේක්", 380),
        ("Chocolate Milk Shake", "චොකලට් මිල්ක් ෂේක්", 350),
        ("Vanilla Milk Shake", "වැනිලා මිල්ක් ෂේක්", 320),
        ("Ice Cream Milk Shake", "අයිස්ක්‍රීම් මිල්ක් ෂේක්", 350),
        ("Kit Kat Milk Shake", "කිට්කැට් මිල්ක් ෂේක්", 400),
        ("Oreo Milk Shake", "ඔරියෝ මිල්ක් ෂේක්", 400),
        ("Biscuit Milk Shake", "බිස්කට් මිල්ක් ෂේක්", 350),
        ("Mango Milk Shake", "අඹ මිල්ක් ෂේක්", 350),
        ("Watermelon Milk Shake", "කොමඩු මිල්ක් ෂේක්", 320),
        ("Avocado Milk Shake", "අලිගැටපේර මිල්ක් ෂේක්", 350),
        ("Papaya Milk Shake", "ගස්ලබු මිල්ක් ෂේක්", 320),
        ("Mix Fruit Milk Shake", "මිශ්‍ර පළතුරු මිල්ක් ෂේක්", 380),
        ("Banana Milk Shake", "කෙසෙල් මිල්ක් ෂේක්", 320),
        ("Dates Milk Shake", "රට ඉඳි මිල්ක් ෂේක්", 380),
        ("Grapes Milk Shake", "මිදි මිල්ක් ෂේක්", 380),
        ("Ice Milo", "අයිස් මයිලෝ", 250),
        ("Ice Coffee", "අයිස් කෝපි", 250),
    ]),
    ("ice-cream", "Ice Cream", "අයිස්ක්‍රීම්", [
        ("Vanilla Ice Cream (3 Scoop)", "වැනිලා අයිස්ක්‍රීම්", 250),
        ("Chocolate Ice Cream (3 Scoop)", "චොකලට් අයිස්ක්‍රීම්", 250),
        ("Strawberry Ice Cream (3 Scoop)", "ස්ට්‍රෝබෙරි අයිස්ක්‍රීම්", 250),
        ("Fruit & Nut Ice Cream", "ෆෘට් ඇන්ඩ් නට් අයිස්ක්‍රීම්", 300),
        ("Mix Ice Cream", "මිශ්‍ර අයිස්ක්‍රීම්", 280),
        ("Ice Cream with Jelly", "අයිස්ක්‍රීම් සමග ජෙලි", 300),
        ("Ice Cream with Corns", "අයිස්කෝන්", 150),
        ("Budget Pack Ice Cream", "බජට් අයිස්ක්‍රීම්", 120),
        ("Café R2 Special Ice Cream", "R2 විශේෂ අයිස්ක්‍රීම්", 380),
        ("Imorich Brand Ice Cream", "ඉමෝරිච් අයිස්ක්‍රීම්", 200),
    ]),
    ("fruit-juice", "Fruit Juice", "පළතුරු ජුස්", [
        ("Orange Juice", "දොඩම් ජුස්", 250),
        ("Mango Juice", "අඹ ජුස්", 280),
        ("Watermelon Juice", "කොමඩු ජුස්", 220),
        ("Pineapple Juice", "අන්නාසි ජුස්", 250),
        ("Papaya Juice", "ගස්ලබු ජුස්", 220),
        ("Avocado Juice", "අලිගැටපේර ජුස්", 280),
        ("Mix Fruit Juice", "මිශ්‍ර පළතුරු ජුස්", 300),
        ("Wood Apple Juice", "දිවුල් ජුස්", 250),
        ("Banana Juice", "කෙසෙල් ජුස්", 220),
        ("Passion Fruit Juice", "පැෂන් ජුස්", 250),
        ("Panidodam Juice", "පැණිදොඩම් ජුස්", 250),
        ("Lime Juice", "දෙහි ජුස්", 200),
        ("Anona Juice", "අනෝන ජුස්", 280),
        ("Grapes Juice", "මිදි ජුස්", 300),
        ("Indian Gooseberry Juice", "නෙල්ලි ජුස්", 220),
    ]),
]

CAROUSEL = [
    ("watermelon-mojito.jpg", "Watermelon Mojito", "කොමඩු මොජිටෝ"),
    ("passion-mojito.jpg", "Passion Mojito", "පැෂන් මොජිටෝ"),
    ("lime-mojito.jpg", "Lime Mojito", "දෙහි මොජිටෝ"),
    ("blackcurrant-mojito.jpg", "Blackcurrant Mojito", "බ්ලැක්කරන්ට් මොජිටෝ"),
    ("orange-mojito.jpg", "Orange Mojito", "ඔරේන්ජ් මොජිටෝ"),
    ("passion-fruit-juice.jpg", "Passion Fruit Juice", "පැෂන් ජුස්"),
    ("chocolate-milkshake.jpg", "Chocolate Milk Shake", "චොකලට් මිල්ක් ෂේක්"),
    ("ice-coffee.jpg", "Ice Coffee", "අයිස් කෝපි"),
]


def esc(s):
    return s.replace("&", "&amp;")


def build_tabs():
    out = []
    for i, (slug, en, si, items) in enumerate(MENU):
        active = " active" if i == 0 else ""
        out.append(
            f'<button class="menu-tab{active}" data-target="panel-{slug}">{esc(en)}<span class="si">{si}</span></button>'
        )
    return "\n".join(out)


def build_panels():
    out = []
    for i, (slug, en, si, items) in enumerate(MENU):
        active = " active" if i == 0 else ""
        rows = []
        for name_en, name_si, price in items:
            rows.append(
                f'''          <div class="menu-item">
            <div class="names"><strong>{esc(name_en)}</strong><span class="si">{name_si}</span></div>
            <div class="price">Rs. {price}</div>
          </div>'''
            )
        rows_html = "\n".join(rows)
        out.append(
            f'''        <div class="menu-panel{active}" id="panel-{slug}">
          <div class="menu-grid">
{rows_html}
          </div>
        </div>'''
        )
    return "\n".join(out)


def build_carousel():
    out = []
    for img, en, si in CAROUSEL:
        out.append(
            f'''        <div class="carousel-card">
          <div class="photo"><img src="images/{img}" alt="{esc(en)} at Café R2 Urubokka" loading="lazy" width="480" height="640"></div>
          <div class="cap"><strong>{esc(en)}</strong><span class="si">{si}</span></div>
        </div>'''
        )
    return "\n".join(out)


def build_menu_schema_text():
    """Plain-text summary for JSON-LD hasMenu / description purposes."""
    cats = [f"{en} ({si})" for _, en, si, _ in MENU]
    return ", ".join(cats)


if __name__ == "__main__":
    with open("menu_tabs.html", "w", encoding="utf-8") as f:
        f.write(build_tabs())
    with open("menu_panels.html", "w", encoding="utf-8") as f:
        f.write(build_panels())
    with open("carousel.html", "w", encoding="utf-8") as f:
        f.write(build_carousel())
    print("Categories:", build_menu_schema_text())
    print("Total items:", sum(len(items) for _, _, _, items in MENU))
