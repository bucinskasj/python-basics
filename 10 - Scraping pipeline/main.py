from utils.extract import extract_full_body_html
from utils.parse import parse_raw_attributes
from utils.process import format_and_transform, save_to_file
from config.tools import get_config


if __name__ == "__main__":
    config = get_config()
    html = extract_full_body_html(
        from_url=config.get('url'),
        wait_for=config.get('container').get('selector')
    )

    nodes = parse_raw_attributes(html, [config.get('container')])

    # tree = HTMLParser(html)

    # divs = tree.css(config.get('container').get('selector'))

    # print(len(divs))
    game_data = []
    for node in nodes.get("store_sale_divs"):
        attrs = parse_raw_attributes(node, config.get('item'))
        attrs = format_and_transform(attrs)
        game_data.append(attrs)
        save_to_file("extract", game_data)
        # title = d.css_first('div[class*="StoreSaleWidgetTitle"]').text()

        # thumbnail = d.css_first(
        #     'img[class*="CapsuleImage"]').attributes.get('src')
        # tags = [a.text()
        #         for a in d.css('div[class*="StoreSaleWidgetTags"] > a')[:5]]
        # release_date = d.css_first(
        #     'div[class*="WidgetReleaseDateAndPlatformCtn"] > div[class*="StoreSaleWidgetRelease"]').text()
        # review_score = d.css_first(
        #     'div[class*="ReviewScoreValue"] > div').text()
        # reviewed_by = d.css_first('div[class*="ReviewScoreCount"]').text()
        # sale_price = d.css_first('div[class*="StoreSalePriceBox"]').text()
        # original_price = d.css_first(
        #     'div[class*="StoreOriginalPrice"]').text()

        # attrs = {
        #     "title": title,
        #     "sale_price": sale_price,
        #     "original_price": original_price,
        #     "review_score": review_score,
        #     "reviewed_by": reviewed_by,
        #     "release_date": release_date,
        #     "tags": tags,
        #     "thumbnail": thumbnail
        # }
