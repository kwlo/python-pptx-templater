from pptx_templater.file_handler import create
from pptx_templater.slides import duplicate_slide, update_text


def _parse_request(source, target, jsonbody):
    for slide in jsonbody.get('slides', []):
        duplicate_slide(source, target, slide['layoutSlideNum'])
        update_text(target.slides[-1], **slide['text'])


def convert(srcpath, destpath, jsonbody):
    source, target = create(srcpath)

    _parse_request(source, target, jsonbody)

    target.save(destpath)
