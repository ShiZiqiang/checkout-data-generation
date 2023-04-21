from pathlib import Path
from typing import List, Dict
import os
import json


def join_mscoco_annotations(dataset_dir: Path):

    for dataset_type in ["train"]:
    #for dataset_type in ["train", "validation", "test"]:
        folder_path = dataset_dir / dataset_type
        output_path = folder_path / "splits.json"
        json_paths = [
            f for f in folder_path.rglob("*.json") if f.name != output_path.name
        ]
        save_joined_mscoco_annotation_file_from_paths_of_single_image_annotations(
            json_paths, output_path
        )


def save_joined_mscoco_annotation_file_from_paths_of_single_image_annotations(
    json_paths: List[Path], output_path: Path
):
    file_dicts = load_mscoco_file_dicts(json_paths)
    final_dict = join_mscoco_annotation_dicts(file_dicts)

    if os.path.exists(output_path):
        os.remove(output_path)
    with open(output_path, "w") as f:
        json.dump(final_dict, f, indent=1)
        #json.dump(final_dict, f)


def load_mscoco_file_dicts(paths: List[Path]) -> List[Dict]:
    file_dicts = []
    for path in paths:
        with path.open("r") as json_file:
            file_dict = json.load(json_file)
            file_dicts.append(file_dict)
    return file_dicts


def join_mscoco_annotation_dicts(annotation_dicts: List[Dict]):
    anno_dict_final = dict()
    anno_dict_final["images"] = join_mscoco_annotation_imgs(annotation_dicts)
    anno_dict_final["annotations"] = join_mscoco_annotation_img_annotations(
        annotation_dicts
    )
    anno_dict_final["categories"] = join_mscoco_annotation_categories(annotation_dicts)


    #anno_dict_final["categories"] = join_mscoco_annotation_categories(annotation_dicts)
    #anno_dict_final["annotations"] = join_mscoco_annotation_img_annotations(
    #    annotation_dicts
    #)
    #anno_dict_final["images"] = join_mscoco_annotation_imgs(annotation_dicts)
    return anno_dict_final


def join_mscoco_annotation_img_annotations(anno_dicts: List[Dict]) -> List:
    annotations = [anno["annotations"] for anno in anno_dicts]
    images = [anno["images"] for anno in anno_dicts]
    mask_id = 0
    for img_id, anno_list_of_img in enumerate(annotations):
        images[img_id][0]["id"] = img_id  # img id stays the same, always just one image
        for anno in anno_list_of_img:
            anno["id"] = mask_id
            anno["image_id"] = img_id
            mask_id += 1
    annotations_final = sum([anno["annotations"] for anno in anno_dicts], [])
    return annotations_final


def join_mscoco_annotation_imgs(anno_dicts: List[Dict]) -> List:
    images = [anno["images"] for anno in anno_dicts]
    images_final = sum([[img for img in img_list] for img_list in images], [])
    return images_final


def join_mscoco_annotation_categories(anno_dicts: List[Dict]) -> List:
    final_categories = []
    categories = [anno["categories"] for anno in anno_dicts]
    category_names = sum(
        [[cat["name"] for cat in cat_list] for cat_list in categories], []
    )
    for name in set(category_names):  # check unique category names
        matching_ids = sum(
            [
                [cat["id"] for cat in cat_list if cat["name"] == name]
                for cat_list in categories
            ],
            [],
        )
        unique_matching_ids = set(matching_ids)
        assert (
            len(unique_matching_ids) == 1
        )  # each name must only be assigned the same id
        curr_category = {"id": unique_matching_ids.pop(), "name": name}
        final_categories.append(curr_category)
    return final_categories


if __name__ == "__main__":


    output_path1 = Path("./data/aicity23_train_scale0.4-0.8_iou0.5")
    # output_path2 = Path("./data/aicity23_train2")
    # output_path3 = Path("./data/aicity23_train3")
    # output_path45 = Path("./data/aicity23_train45")
    #join_mscoco_annotations(output_path)

    #output_path = Path("./") / "train_splits.json"
    output_path = Path("./") / "instances_train.json"
    for dataset_type in ["train"]:
    #for dataset_type in ["train", "validation", "test"]:
        folder_path1 = output_path1 / dataset_type

        json_paths1 = [
            f for f in folder_path1.rglob("*.json") if f.name != output_path.name
        ]
    #
    # for dataset_type in ["train2"]:
    #     folder_path2 = output_path2 / dataset_type
    #
    #     json_paths2 = [
    #         f for f in folder_path2.rglob("*.json") if f.name != output_path.name
    #     ]
    #
    # for dataset_type in ["train3"]:
    #     folder_path3 = output_path3 / dataset_type
    #
    #     json_paths3 = [
    #         f for f in folder_path3.rglob("*.json") if f.name != output_path.name
    #     ]
    #
    # for dataset_type in ["train45"]:
    #     folder_path45 = output_path45 / dataset_type
    #
    #     json_paths45 = [
    #         f for f in folder_path45.rglob("*.json") if f.name != output_path.name
    #     ]

        #print(len(json_paths1 + json_paths2 + json_paths3 + json_paths45))


    save_joined_mscoco_annotation_file_from_paths_of_single_image_annotations(
        json_paths1, output_path
    )


    # output_path1 = Path("./data/aicity23_train1")
    # output_path2 = Path("./data/aicity23_train2")
    # output_path3 = Path("./data/aicity23_train3")
    # output_path45 = Path("./data/aicity23_train45")
    # #join_mscoco_annotations(output_path)
    #
    # output_path = Path("./") / "train_splits.json"
    # for dataset_type in ["train1"]:
    # #for dataset_type in ["train", "validation", "test"]:
    #     folder_path1 = output_path1 / dataset_type
    #
    #     json_paths1 = [
    #         f for f in folder_path1.rglob("*.json") if f.name != output_path.name
    #     ]
    #
    # for dataset_type in ["train2"]:
    #     folder_path2 = output_path2 / dataset_type
    #
    #     json_paths2 = [
    #         f for f in folder_path2.rglob("*.json") if f.name != output_path.name
    #     ]
    #
    # for dataset_type in ["train3"]:
    #     folder_path3 = output_path3 / dataset_type
    #
    #     json_paths3 = [
    #         f for f in folder_path3.rglob("*.json") if f.name != output_path.name
    #     ]
    #
    # for dataset_type in ["train45"]:
    #     folder_path45 = output_path45 / dataset_type
    #
    #     json_paths45 = [
    #         f for f in folder_path45.rglob("*.json") if f.name != output_path.name
    #     ]
    #
    #     #print(len(json_paths1 + json_paths2 + json_paths3 + json_paths45))
    #
    #
    # save_joined_mscoco_annotation_file_from_paths_of_single_image_annotations(
    #     json_paths1 + json_paths2 + json_paths3 + json_paths45, output_path
    # )
