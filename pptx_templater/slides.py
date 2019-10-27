from copy import deepcopy

# from pptx.parts.chart import ChartPart
# from pptx.parts.embeddedpackage import EmbeddedXlsxPart
from pptx_templater.text_parser import render


def update_text(slide, **kwargs):
    for shape in slide.shapes:
        if not shape.has_text_frame:
            continue
        for paragraph in shape.text_frame.paragraphs:
            for run in paragraph.runs:
                run.text = render(run.text, **kwargs)


def clear(presentation):
    slides = reversed([(idx, sld.rId) for idx, sld in enumerate(presentation.slides._sldIdLst)])

    for (idx, rId) in slides:
        presentation.part.drop_rel(rId)
        del presentation.slides._sldIdLst[idx]


def _get_blank_slide_layout(pres):
    layout_items_count = [len(layout.placeholders)
                          for layout in pres.slide_layouts]
    min_items = min(layout_items_count)
    blank_layout_id = layout_items_count.index(min_items)
    return pres.slide_layouts[blank_layout_id]


def duplicate_slide(source, target, index):
    """Duplicate the slide with the given index in pres.

    Adds slide to the end of the presentation"""
    source_slide = source.slides[index]
    blank_slide_layout = _get_blank_slide_layout(target)
    dest = target.slides.add_slide(blank_slide_layout)

    for shape in source_slide.shapes:
        newel = deepcopy(shape.element)
        dest.shapes._spTree.insert_element_before(newel, 'p:extLst')
'''
    for key, value in source_slide.part.rels.items():
        # Make sure we don't copy a notesSlide relation as that won't exist
        if "notesSlide" not in value.reltype:
            _target = value._target
            # if the relationship was a chart, we need to duplicate the embedded chart part and xlsx
            if "chart" in value.reltype:
                partname = _target.package.next_partname(
                    ChartPart.partname_template)
                xlsx_blob = _target.chart_workbook.xlsx_part.blob
                _target = ChartPart(partname, _target.content_type,
                                   deepcopy(_target._element), package=_target.package)

                _target.chart_workbook.xlsx_part = EmbeddedXlsxPart.new(
                    xlsx_blob, _target.package)

            dest.part.rels.add_relationship(value.reltype,
                                            _target,
                                            value.rId)
'''