def run():
    my_list = [1,"hello",True,4.5]
    my_dict = {"firstname": "Ruben","lastname": "Marquez"}

    super_list = [
        {"firstname": "Ruben","lastname": "Marquez"},
        {"firstname": "Marina","lastname": "Eiri"},
        {"firstname": "Anais","lastname": "Kinomoto"},
        {"firstname": "Lucy","lastname": "Li"},
        {"firstname": "Sagato","lastname": "Shaoran"}
    ]
    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items()
        print(key, "-", value)


if __name__ == '__main__':  
    run()