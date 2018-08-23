import tensorflow as tf
from  model import VDSR
flags = tf.app.flags
FLAGS = flags.FLAGS
flags.DEFINE_integer("epoch", 1500, "Number of epoch")
flags.DEFINE_integer("image_size", 41, "The size of image input")
flags.DEFINE_integer("label_size", 41, "The size of image output")
flags.DEFINE_integer("c_dim", 3, "The size of channel")
flags.DEFINE_boolean("is_train", True, "if the train")
flags.DEFINE_integer("scale", 3, "the size of scale factor for preprocessing input image")
flags.DEFINE_integer("stride", 41, "the size of stride") ##because output is 33 * 33
flags.DEFINE_string("checkpoint_dir", "checkpoint", "Name of checkpoint directory")
flags.DEFINE_float("learning_rate", 1e-4 , "The learning rate")
flags.DEFINE_integer("batch_size", 64, "the size of batch")
flags.DEFINE_string("result_dir", "result", "Name of result directory")
flags.DEFINE_string("test_img", "", "test_img")
flags.DEFINE_float("clip_grad", 1e-1 , "The clip gradient number")
flags.DEFINE_integer("layer", 20, "the size of layer")



def main(_): #?
    with tf.Session() as sess:
        vdsr = VDSR(sess,
                      image_size = FLAGS.image_size,
                      label_size = FLAGS.label_size,
                      layer = FLAGS.layer,
                      c_dim = FLAGS.c_dim
                      # config = FLAGS
                   )

        vdsr.train(FLAGS)

if __name__=='__main__':
    tf.app.run() # parse the command argument , the call the main function
