def get_diff_blocks(document_right, document_left):
    diff_blocks = {}
    block_index = -1

    if len(document_right) != len(document_left):
        raise ValueError("Could not compare different size data.")

    for index, (x, y) in enumerate(zip(document_right, document_left)):
        if x != y:
            if block_index == -1:
                block_index = index
                diff_blocks[block_index] = 0
            diff_blocks[block_index] += 1
        else:
            block_index = -1

    return diff_blocks
